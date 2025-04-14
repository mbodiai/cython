import base64
import base64 as base64lib
import hashlib
import logging
import time
import traceback
from functools import lru_cache, update_wrapper
from pathlib import Path
from threading import RLock
from typing import (
    TYPE_CHECKING,
    Any,
    Callable,
    Literal,
    NamedTuple,
    ParamSpec,
    Tuple,
    TypedDict,
    TypeVar,
)

# Import NDArray from numpy.typing
import numpy as np
import PIL.Image as PILModule
from PIL.Image import Image as PILImage
from typing_extensions import TypeVarTuple, overload

from mbcore.import_utils import smart_import
from mbcore.utils.type_utils import NumPyArrayNumeric

h = hashlib.new("sha256")
H = TypeVar("H", bound=int)
W = TypeVar("W", bound=int)
P = ParamSpec("P")
R = TypeVar("R")
Ts = TypeVarTuple("Ts")
DT_co = TypeVar("DT_co", bound=np.dtype)

Float64 = np.float64
Float = np.float32 | np.float64
Int = np.int32 | np.int64 | np.uint32 | np.uint64 | np.int8 | np.int16 | np.uint8 | np.uint16
Bool = np.bool_
Int8 = np.int8
Int16 = np.int16
Int32 = np.int32
Int64 = np.int64
UInt8 = np.uint8
UInt16 = np.uint16
UInt32 = np.uint32
UInt64 = np.uint64
Sz = Any
sz = Literal


class _CacheInfo(NamedTuple):
    hits: int
    misses: int
    maxsize: int
    currsize: int


if TYPE_CHECKING:
    from mbodios.geometry.array import array
    from mbodios.types.sense.image import Image
else:
    from typing_extensions import Protocol, Unpack, runtime_checkable

    @runtime_checkable
    class array(Protocol[Unpack[Ts], DT_co]): ...


def detect_changes(old_block, new_block, method: Literal["hash", "histogram"] = "hash") -> bool:
    if not TYPE_CHECKING:
        cv2 = smart_import("cv2")
        smart_import("cv2.img_hash")
        smart_import("cv2.imgproc")
    if method == "hash":
        hash_old = cv2.img_hash.averageHash(old_block)
        hash_new = cv2.img_hash.averageHash(new_block)
        return not np.array_equal(hash_old, hash_new)
    if method == "histogram":
        hist_old = cv2.calcHist([old_block], [0], None, [256], [0, 256])
        hist_new = cv2.calcHist([new_block], [0], None, [256], [0, 256])
        return cv2.compareHist(hist_old, hist_new, cv2.HISTCMP_CORREL) < 0.99
    raise ValueError(f"Unknown method: {method}. Use 'hash' or 'histogram'.")


def warn_opencv_contrib():
    logging.warning("OpenCV contrib modules are not installed. Some functions may not work as expected.")


def error_opencv_contrib():
    if smart_import("cv2.img_hash", "lazy") == Any:
        raise ImportError("cv2.img_hash not found. Please install the  `opencv-contrib-python`")


class HashMethods(TypedDict):
    PHash: Callable[[NumPyArrayNumeric], NumPyArrayNumeric]
    AverageHash: Callable[[NumPyArrayNumeric], NumPyArrayNumeric]
    BlockMeanHash: Callable[[NumPyArrayNumeric], NumPyArrayNumeric]
    ColorMomentHash: Callable[[NumPyArrayNumeric], NumPyArrayNumeric]
    MarrHildrethHash: Callable[[NumPyArrayNumeric], NumPyArrayNumeric]
    RadialVarianceHash: Callable[[NumPyArrayNumeric], NumPyArrayNumeric]
    SHA256: Callable[[NumPyArrayNumeric], NumPyArrayNumeric]
    NoHash: Callable[[NumPyArrayNumeric], NumPyArrayNumeric]


def hash_methods() -> HashMethods:
    """Returns a dictionary of hash methods."""
    error_opencv_contrib()
    if TYPE_CHECKING:
        from cv2.img_hash import (
            averageHash,
            blockMeanHash,
            colorMomentHash,
            marrHildrethHash,
            pHash,
            radialVarianceHash,
        )
    else:
        averageHash = smart_import("cv2.img_hash.averageHash")  # noqa: N806
        blockMeanHash = smart_import("cv2.img_hash.blockMeanHash")  # noqa: N806
        colorMomentHash = smart_import("cv2.img_hash.colorMomentHash")  # noqa: N806
        marrHildrethHash = smart_import("cv2.img_hash.marrHildrethHash")  # noqa: N806
        pHash = smart_import("cv2.img_hash.pHash")  # noqa: N806
        radialVarianceHash = smart_import("cv2.img_hash.radialVarianceHash")  # noqa: N806

    def sha256(array: NumPyArrayNumeric) -> NumPyArrayNumeric:
        h = hashlib.new("sha256")
        h.update(array.tobytes())
        return np.frombuffer(h.digest(), dtype=np.uint8)

    return {
        "PHash": pHash,
        "AverageHash": averageHash,
        "BlockMeanHash": blockMeanHash,
        "ColorMomentHash": colorMomentHash,
        "MarrHildrethHash": marrHildrethHash,
        "RadialVarianceHash": radialVarianceHash,
        "SHA256": sha256,
        "NoHash": lambda x: x,
    }


def cached_semantic_hash(
    image: array[H, W, sz[3], Int] | array[H, W, sz[1], Int] | array[H, W, Int],
    method: Literal[
        "PHash",
        "AverageHash",
        "BlockMeanHash",
        "ColorMomentHash",
        "MarrHildrethHash",
        "RadialVarianceHash",
        "SHA256",
        "NoHash",
    ] = "PHash",
) -> bytes:
    """Compute and cache the semantic hash of an image."""
    return hash_methods()[method](np.asarray(image)).tobytes()


class _HashedSeq(list):
    """This class guarantees that hash() will be called no more than once per element.

    This is important because the lru_cache() will hash the key multiple times on a cache miss.
    """

    __slots__ = "hashvalue"

    def __init__(self, tup, hash=hash):
        self[:] = tup
        self.hashvalue = hash(tup)

    def __hash__(self):
        return self.hashvalue


@overload
def lru_cache(func: Callable[P, R]) -> Callable[P, R]: ...
@overload
def lru_cache(maxsize=128, typed=False) -> Callable[[Callable[P, R]], Callable[P, R]]: ...
def lru_cache(*args, **kwargs) -> Any:
    """Least-recently-used cache decorator."""
    if len(args) == 1 and callable(args[0]):
        return lru_cache()(args[0])
    arglist = list(args)
    maxsize = kwargs.get("maxsize", arglist.pop(0) if arglist else 128)
    typed = kwargs.get("typed", arglist.pop(0) if arglist else False)
    if isinstance(maxsize, int):
        if maxsize < 0:
            maxsize = 0
    elif callable(maxsize) and isinstance(typed, bool):
        user_function, maxsize = maxsize, 128
        wrapper = _lru_cache_wrapper(user_function, maxsize, typed, _CacheInfo)
        wrapper.cache_parameters = lambda: {"maxsize": maxsize, "typed": typed}
        return update_wrapper(wrapper, user_function)
    elif maxsize is not None:
        raise TypeError("Expected first argument to be an integer, a callable, or None.")

    def decorating_function(user_function: Callable[P, R]) -> Callable[P, R]:
        wrapper = _lru_cache_wrapper(user_function, maxsize, typed, _CacheInfo)
        wrapper.cache_parameters = lambda: {"maxsize": maxsize, "typed": typed}
        return update_wrapper(wrapper, user_function)  # type: ignore

    return decorating_function


# Helper for cache keys
def _make_key(args, kwds, typed, kwd_mark=(object(),), fasttypes={int, str}, tuple=tuple, type=type, len=len):
    """Modified to handle numpy arrays by converting them to bytes."""

    def _convert_numpy(arg):
        if isinstance(arg, np.ndarray):
            return arg.tobytes()
        return arg

    args = tuple(_convert_numpy(arg) for arg in args)
    key = args
    if kwds:
        key += kwd_mark
        for item in kwds.items():
            key += (_convert_numpy(item[0]), _convert_numpy(item[1]))
    if typed:
        key += tuple(type(v) for v in args)
        if kwds:
            key += tuple(type(v) for v in kwds.values())
    elif len(key) == 1 and type(key[0]) in fasttypes:
        return key[0]
    return _HashedSeq(key)


def _lru_cache_wrapper(user_function, maxsize, typed, _CacheInfo):
    # Constants shared by all lru cache instances:
    sentinel = object()  # unique object used to signal cache misses
    make_key = _make_key  # build a key from the function arguments
    PREV, NEXT, KEY, RESULT = 0, 1, 2, 3  # names for the link fields

    cache = {}
    hits = misses = 0
    full = False
    cache_get = cache.get  # bound method to lookup a key or return None
    cache_len = cache.__len__  # get cache size without calling len()
    lock = RLock()  # because linkedlist updates aren't threadsafe
    root = []  # root of the circular doubly linked list
    root[:] = [root, root, None, None]  # initialize by pointing to self

    if maxsize == 0:

        def wrapper(*args, **kwds):
            # No caching -- just a statistics update
            nonlocal misses
            misses += 1
            result = user_function(*args, **kwds)
            return result

    elif maxsize is None:

        def wrapper(*args, **kwds):
            # Simple caching without ordering or size limit
            nonlocal hits, misses
            key = make_key(args, kwds, typed)
            result = cache_get(key, sentinel)
            if result is not sentinel:
                hits += 1
                return result
            misses += 1
            result = user_function(*args, **kwds)
            cache[key] = result
            return result

    else:

        def wrapper(*args, **kwds):
            # Size limited caching that tracks accesses by recency
            nonlocal root, hits, misses, full
            key = make_key(args, kwds, typed)
            with lock:
                link = cache_get(key)
                if link is not None:
                    # Move the link to the front of the circular queue
                    link_prev, link_next, _key, result = link
                    link_prev[NEXT] = link_next
                    link_next[PREV] = link_prev
                    last = root[PREV]
                    last[NEXT] = root[PREV] = link
                    link[PREV] = last
                    link[NEXT] = root
                    hits += 1
                    return result
                misses += 1
            result = user_function(*args, **kwds)
            with lock:
                if key in cache:
                    # Getting here means that this same key was added to the
                    # cache while the lock was released.  Since the link
                    # update is already done, we need only return the
                    # computed result and update the count of misses.
                    pass
                elif full:
                    # Use the old root to store the new key and result.
                    oldroot = root
                    oldroot[KEY] = key
                    oldroot[RESULT] = result
                    # Empty the oldest link and make it the new root.
                    # Keep a reference to the old key and old result to
                    # prevent their ref counts from going to zero during the
                    # update. That will prevent potentially arbitrary object
                    # clean-up code (i.e. __del__) from running while we're
                    # still adjusting the links.
                    root = oldroot[NEXT]
                    oldkey = root[KEY]
                    root[RESULT]
                    root[KEY] = root[RESULT] = None
                    # Now update the cache dictionary.
                    del cache[oldkey]
                    # Save the potentially reentrant cache[key] assignment
                    # for last, after the root and links have been put in
                    # a consistent state.
                    cache[key] = oldroot
                else:
                    # Put result in a new link at the front of the queue.
                    last = root[PREV]
                    link = [last, root, key, result]
                    last[NEXT] = root[PREV] = cache[key] = link
                    # Use the cache_len bound method instead of the len() function
                    # which could potentially be wrapped in an lru_cache itself.
                    full = cache_len() >= maxsize
            return result

    def cache_info():
        """Report cache statistics."""
        with lock:
            return _CacheInfo(hits, misses, maxsize, cache_len())

    def cache_clear():
        """Clear the cache and cache statistics."""
        nonlocal hits, misses, full
        with lock:
            cache.clear()
            root[:] = [root, root, None, None]
            hits = misses = 0
            full = False

    wrapper.cache_info = cache_info
    wrapper.cache_clear = cache_clear
    return wrapper


# @lru_cache(maxsize=128)
# def load_url(url: "str | Image") -> array[H, W, Int]:
#     """Downloads an image from a URL or decodes it from a base64 data URI.

#     Args:
#         url (str): The URL of the image to download, or a base64 data URI.
#         dtype: The data type for the resulting array.

#     Returns:
#         np.ndarray: The image as a numpy array.
#     """
#     if not TYPE_CHECKING:
#         Image = smart_import("mbodios.types.sense.image.Image")
#     str_url = str(url.url if isinstance(url, Image) else url)
#     if str_url is None:
#         raise ValueError("URL is None")
#     if isinstance(str_url,str) and str_url.startswith("data:image"):
#         # Extract the base64 part of the data URI
#         base64_str = str_url.split(";base64,", 1)[1]
#         return loads(base64.b64decode(base64_str))

#     try:
#         # Open the URL and read the image data
#         headers = {"User-Agent": "Mozilla/5.0"}
#         if not str_url.startswith("http"):
#             raise ValueError("URL must start with 'http' or 'https'.")
#         request = urllib.request.Request(str_url, None, headers)
#         response = urllib.request.urlopen(request)
#         data = response.read()
#         return loads(data)
#     except Exception as e:
#         logging.warning(f"Failed to load image from URL: {url}. {e}")
#         raise ValueError(f"Failed to load image from URL: {url}. {e}") from None


@lru_cache(maxsize=128)
def to_url(
    image: "array[H, W, np.integer] | array[H,W,sz[3],np.integer] | array[H,W,sz[1],np.integer] | Image[H,W]",
    encoding: Literal["png", "jpg", "jpeg", "bmp", "tiff"] = "png",
) -> str:
    """Convert image array to URL string."""
    if not TYPE_CHECKING:
        Image = smart_import("mbodios.types.sense.image.Image")
    try:
        if isinstance(image, Image):
            encoding = encoding or image.encoding
            array = image.array
        else:
            array = image
        if array is None:
            return ...
        img_bytes = to_bytes(array, encoding=encoding)
        img_base64 = base64.b64encode(img_bytes).decode()
        return f"data:image/{encoding};base64,{img_base64}"
    except Exception as e:
        logging.error(f"Failed to convert image to URL: {e}")
        raise


@lru_cache(maxsize=128)
def load_url(
    url: str,
    size: Tuple[int, int] | None = None,
    encoding: str | None = None,
    mode: Literal["RGB", "RGBA", "L", "P", "CMYK", "YCbCr", "I", "F"] | None = None,
    **kwargs,
) -> array[H, W, Int]:
    """Downloads an image from a URL or decodes it from a base64 data URI.

    This method can handle both regular image URLs and base64 data URIs.
    For regular URLs, it downloads the image data. For base64 data URIs,
    it decodes the data directly. It's useful for fetching images from
    the web or working with inline image data.

    Args:
        url (str): The URL of the image to download, or a base64 data URI.
        size (Optional[Tuple[int, int]]): The desired size of the image as a (width, height) tuple. Defaults to None.
        encoding (Optional[str]): The encoding format of the image. Defaults to None.
        mode (Optional[str]): The mode to use for the image. Defaults to None.
        **kwargs: Additional keyword arguments.

    Returns:
        PIL.Image.Image | None: The downloaded and decoded image as a PIL Image object,
                                or None if the download fails or is cancelled.

    Example:
        >>> image = Image.load_url("https://example.com/image.jpg")
        >>> if image:
        ...     print(f"Image size: {image.size}")
        ... else:
        ...     print("Failed to load image")

        >>> data_uri = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAACklEQVR4nGMAAQAABQABDQottAAAAABJRU5ErkJggg=="
        >>> image = Image.load_url(data_uri)
        >>> if image:
        ...     print(f"Image size: {image.size}")
        ... else:
        ...     print("Failed to load image")

    """
    from urllib.request import Request, urlopen

    from mbodios.types.sense.image import Image

    if isinstance(url, Image):
        url = url.url
    user_agent = "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7"
    headers = {"User-Agent": user_agent}
    if url.startswith("data:image/"):
        return from_base64(url, encoding=encoding, size=size, mode=mode)
    if not url.startswith(("http:", "https:")):
        msg = "URL must start with 'http' or 'https'."
        raise ValueError(msg)

    if not url.endswith((".jpg", ".jpeg", ".png", ".bmp", ".gif")) and not url.split("?")[0].endswith(
        (".jpg", ".jpeg", ".png", ".bmp", ".gif"),
    ):
        if url.find("huggingface.co") != -1:
            logging.warning("URL not ending with a valid image extension.")

        else:
            msg = f"URL must end with a valid image extension: {url[:20]}...{url[-20:]}"
            raise ValueError(msg)

    with urlopen(Request(url, None, headers)) as response:  # noqa
        data = response.read()
        return from_bytes(data, size, mode, encoding=encoding)


# @lru_cache(maxsize=128)
def from_base64(
    arg: str,
    encoding: str | None = None,
    size: Tuple[int, int] | None = None,
    mode: Literal["RGB", "RGBA", "L", "P", "CMYK", "YCbCr", "I", "F"] | None = "RGB",
    **kwargs,
) -> array[H, W, Int]:
    """Decodes a base64 string to an image array efficiently with a single processing path.

    Args:
        arg: The base64-encoded string or data URI
        encoding: The encoding format (determines bit depth handling)
        size: Optional tuple of (width, height) to resize the image to
        mode: Color mode for output array ('RGB', 'RGBA', 'L', etc.)

    Returns:
        NumPy array containing the decoded image in requested format

    """
    if not TYPE_CHECKING:
        smart_import("cv2")
        Image = smart_import("mbodios.types.sense.image.Image")
    if isinstance(arg, Image):
        arg = arg.base64
    # Extract the base64 part and encoding if this is a data URI
    if ";" in arg and "base64," in arg:
        if not encoding and "data:image" in arg:
            mime_type = arg.split("data:image/", 1)[1].split(";", 1)[0]
            encoding = mime_type
        if ";" in arg:
            base64_str = arg.split(";base64,", 1)[1]
        else:
            base64_str = arg
    else:
        base64_str = arg

    # Add padding if needed (before decoding)
    padding = len(base64_str) % 4
    if padding:
        base64_str += "=" * (4 - padding)

    # Decode base64 to bytes
    img_bytes = base64.b64decode(base64_str, validate=True)

    return from_bytes(img_bytes, size, mode, encoding)


def from_bytes(
    arg: bytes,
    size: Tuple[int, int] | None = None,
    mode: Literal["RGB", "RGBA", "L", "P", "CMYK", "YCbCr", "I", "F", "I16"] | None = "RGB",
    encoding: Literal["png", "jpg", "jpeg", "bmp", "tiff"] | None = None,
    **kwargs,
) -> array:
    if TYPE_CHECKING:
        import imghdr
        import io

        import cv2
        import numpy as np
        from PIL import Image
    else:
        cv2 = smart_import("cv2")
        np = smart_import("numpy")
        Image = smart_import("PIL.Image")
        io = smart_import("io")
        imghdr = smart_import("imghdr")

    # Validate encoding vs header
    detected = imghdr.what(None, h=arg)

    if mode == "I16":
        arr = np.frombuffer(arg, dtype=np.uint16)
    elif mode == "F":
        arr = np.frombuffer(arg, dtype=np.float32)
    elif mode == "I":
        arr = np.frombuffer(arg, dtype=np.int32)
    else:
        arr = np.frombuffer(arg, dtype=np.uint8)
    read_flag = cv2.IMREAD_COLOR if mode in ("RGB", "YCbCr", "P", "CMYK") else cv2.IMREAD_UNCHANGED
    img = cv2.imdecode(arr, read_flag)
    if img is None:
        raise ValueError("Failed to decode image data (OpenCV returned None)")

    # Color mode conversions
    if mode == "RGB" and img.ndim == 3 and img.shape[2] == 3:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    elif mode == "RGBA" and img.ndim == 3 and img.shape[2] == 4:
        img = cv2.cvtColor(img, cv2.COLOR_BGRA2RGBA)
    elif mode == "YCbCr":
        img = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
    elif mode == "CMYK":
        img = np.array(Image.open(io.BytesIO(arg)).convert("CMYK"))
    elif mode == "P":
        img = np.array(Image.open(io.BytesIO(arg)).convert("P"))

    # Resize if requested
    if size and tuple(img.shape[:2]) != size:
        img = cv2.resize(img, size[::-1], interpolation=cv2.INTER_LANCZOS4)

    if detected and encoding and detected != encoding:
        return np.array(to_pil(img, encoding=encoding).convert(mode))
    return img


# @lru_cache(maxsize=128)
def loads(
    bytes_data: bytes | str | Path,
    size: Tuple[H, W] | None = None,
    mode: Literal["RGB", "RGBA", "L", "P", "CMYK", "YCbCr", "I", "F"] | None = "RGB",
    encoding: Literal["png", "jpg", "jpeg", "bmp", "tiff"] | None = "jpeg",
) -> array[H, W, Int]:
    """Creates an image array from bytes or base64 string.

    OpenCV loads images in BGR format, but this function converts them to RGB
    to maintain consistency with the rest of the library.

    Args:
        bytes_data: The bytes or base64 string to convert to a numpy array.
        size: Optional tuple of (width, height) to resize the image to.

    Returns:
        np.ndarray: RGB image array with shape (height, width, channels)

    """
    if not TYPE_CHECKING:
        smart_import("cv2")
        Path = smart_import("pathlib.Path")

    if isinstance(bytes_data, bytes):
        return from_bytes(bytes_data, size, mode, encoding)
    if isinstance(bytes_data, Path) or (isinstance(bytes_data, str) and Path(bytes_data[:100]).exists()):
        return from_path(bytes_data, size)
    if isinstance(bytes_data, str) and bytes_data.startswith("http"):
        return load_url(url=bytes_data, size=size, encoding=encoding, mode=mode)
    if isinstance(bytes_data, str):
        return from_base64(arg=bytes_data, size=size, encoding=encoding, mode=mode)

    raise ValueError(f"Expected bytes, got {type(bytes_data)}")


@lru_cache(maxsize=128)
def from_pil(
    pil_image: bytes,
    size: Tuple[H, W] | None = None,
    mode: Literal["RGB", "RGBA", "L", "P", "CMYK", "YCbCr", "I", "F"] | None = "RGB",
    encoding: Literal["png", "jpg", "jpeg", "bmp", "tiff", "gif"] | None = "png",
) -> array[H, W, Int]:
    """Converts a PIL image to a numpy array.

    Args:
        pil_image (Any): The PIL image to convert.
        dtype: The data type for the resulting array.

    Returns:
        np.ndarray: The image as a numpy array.

    """
    if not TYPE_CHECKING:
        cv2 = smart_import("cv2")
    else:
        pass
    arr = np.array(PILModule.open(pil_image).convert(mode))
    if size is not None and tuple(arr.shape[:2]) != size:
        arr = cv2.resize(arr, size[::-1], interpolation=cv2.INTER_LANCZOS4)
    return arr


@lru_cache(maxsize=128)
def from_path(path: str | bytes | Path, size: Tuple[H, W] | None = None) -> array[H, W, Int]:
    """Loads an image from a file path using OpenCV.

    Args:
        path: File path to load the image from.
        size: Optional tuple of (width, height) to resize the image to.

    Returns:
        np.ndarray: RGB image array with shape (height, width, channels)

    """
    if TYPE_CHECKING:
        from cv2 import IMREAD_COLOR, imread
    else:
        imread = smart_import("cv2.imread")
        IMREAD_COLOR = smart_import("cv2.IMREAD_COLOR")
        cv2 = smart_import("cv2")

    # Convert path to absolute Path object
    try:
        path_obj = Path(str(path)).absolute()
        if not path_obj.exists():
            raise FileNotFoundError(f"Image file not found: {path_obj}")
        if not path_obj.is_file():
            raise ValueError(f"Path is not a file: {path_obj}")

        # Read the image from the file path using OpenCV (returns BGR)
        arr = imread(str(path_obj), IMREAD_COLOR)
        if arr is None:
            raise ValueError(f"OpenCV failed to decode image at: {path_obj}")

        # API BOUNDARY: Convert from BGR (OpenCV) to RGB (internal format)
        rgb_arr = cv2.cvtColor(arr, cv2.COLOR_BGR2RGB)

        # Resize if needed
        if size is not None:
            # Size is (width, height) which matches cv2.resize expectations
            rgb_arr = cv2.resize(rgb_arr, size, interpolation=cv2.INTER_LANCZOS4)

        return np.asarray(rgb_arr)
    except Exception as e:
        logging.error(f"Error loading image from {path}: {str(e)}\n{traceback.format_exc()}")
        raise


# @lru_cache(maxsize=128)
def to_bytes(
    image: "array",
    path: str | None = None,
    encoding: Literal["png", "jpg", "jpeg", "bmp", "tiff", "gif"] | None = "png",
    quality: int = 95,
) -> bytes:
    """Converts an image array or Image-like object to encoded bytes."""
    if not TYPE_CHECKING:
        cv2 = smart_import("cv2")
        np = smart_import("numpy")
        Path = smart_import("pathlib.Path")
        smart_import("mbodios.types.sense.image.Image")
        smart_import("PIL.Image")
        io = smart_import("io")
        Image = smart_import("mbodios.types.sense.image.Image")
        from mbcore.types import exists
    else:
        from pathlib import Path

        from mbodios.types.sense.image import Image

        from mbcore.types import exists

    if image is None or (isinstance(image, Image) and not exists(image.array)):
        return ...

    # Determine encoding and extract array
    encoding_used = (getattr(image, "encoding", None) or encoding or "png").lower()
    if isinstance(image, Image):
        array_to_use = np.asarray(image.array)
        from mbcore.types import exists

        if not exists(array_to_use):
            return ...
    else:
        array_to_use = np.asarray(image)

    if array_to_use is None or array_to_use.size == 0 or not exists(array_to_use):
        return ...

    # Handle GIF (not supported by OpenCV)
    if encoding_used == "gif":
        img = PILModule.fromarray(array_to_use)
        buf = io.BytesIO()
        img.save(buf, format="GIF")
        result = buf.getvalue()
        if path:
            Path(path).write_bytes(result)
        return result

    # Normalize JPEG alias
    if encoding_used == "jpg":
        encoding_used = "jpeg"

    if not exists(array_to_use):
        return ...

    try:
        # Convert RGB to BGR for OpenCV if needed
        if array_to_use.ndim == 3 and array_to_use.shape[2] == 3:
            array_bgr = cv2.cvtColor(array_to_use, cv2.COLOR_RGB2BGR)
        else:
            array_bgr = array_to_use

        array_bgr = np.ascontiguousarray(array_bgr)

        # Optional params for encoding
        params = []
        if encoding_used == "jpeg":
            params = [int(cv2.IMWRITE_JPEG_QUALITY), quality]

        success, img_bytes = cv2.imencode(f".{encoding_used}", array_bgr, params)
        if not success:
            return ...

        result = img_bytes.tobytes()

        if path:
            Path(path).write_bytes(result)

        return result

    except Exception as e:
        import logging

        logging.error(f"Failed to convert image to bytes: {e}")
        raise


def to_base64(
    image: "array[H, W, np.integer] | array[H,W,sz[3],np.integer] | array[H,W,sz[1],np.integer] | Image[H,W] | np.ndarray",
    path: str | None = None,
    encoding: Literal["png", "jpg", "jpeg", "bmp", "tiff", "gif"] | None = "png",
) -> str:
    """Converts an image array to a base64 string.

    Returns a complete data URI string (e.g., "data:image/png;base64,...")

    Args:
        image: The image to convert (RGB format expected).
        path: Optional path to save the bytes to.
        encoding: The encoding format to use.

    Returns:
        str: The data URI containing the base64-encoded image.

    """
    if not TYPE_CHECKING:
        Image = smart_import("mbodios.types.sense.image.Image")
        from mbcore.types import exists
    if image is None:
        return ...
    if isinstance(image, Image) and not exists(image.array):
        return ...

    # Get encoding from Image object if available
    if hasattr(image, "encoding") and hasattr(type(image), "encoding"):
        encoding = getattr(image, "encoding", encoding) or "png"

    # Convert to bytes first
    img_bytes = image.tobytes()

    # Encode as base64 and format as data URI
    base64_str = base64lib.b64encode(img_bytes).decode("utf-8")
    return f"data:image/{encoding};base64,{base64_str}"


def to_pil(
    image: "Image",
    mode: Literal["RGB", "RGBA", "L", "P", "CMYK", "YCbCr", "I", "F"] | None = None,
    encoding: Literal["png", "jpg", "jpeg", "bmp", "tiff", "gif"] | None = None,
) -> "PILImage":
    """Converts a numpy array to a PIL image.

    Args:
        image (np.array): The image array to convert.

    Returns:
        Any: The PIL image.

    """
    from mbodios.types.sense.image import Image

    from mbcore.types import exists

    if not exists(image):
        return ...
    if isinstance(image, Image) and not exists(image.array):
        return ...
    if not TYPE_CHECKING:
        PILModule = smart_import("PIL.Image")
    else:
        from PIL import Image
    array = image.array if hasattr(image, "array") else image
    return PILModule.fromarray(array, mode=mode)


def error(
    original: array[H, W, Int], modified: array[H, W, Int], metric: Literal["mse", "cosine", "hamming", "mae"] = "mse",
) -> float:
    if metric == "cosine":
        similarity = np.dot(original, modified) / (np.linalg.norm(original) * np.linalg.norm(modified))
        return 1 - similarity
    if metric == "hamming":
        return np.mean(original != modified)
    if metric == "mae":
        return np.mean(np.abs(np.asarray(original) - np.asarray(modified)).astype(float)).astype(float)
    if metric == "mse":
        return np.mean((np.asarray(original) - np.asarray(modified)) ** 2).astype(float)
    raise ValueError(f"Unknown metric: {metric}")


def benchmark_hash_method(
    hash_func: Callable[[NumPyArrayNumeric], NumPyArrayNumeric],
    input_data: NumPyArrayNumeric,
    modified_data: NumPyArrayNumeric | None = None,
    iterations: int = 10,
):
    start = time.time()
    hash_value = None
    try:
        for _ in range(iterations):
            hash_value = hash_func(input_data)

        end = time.time()

        reconstruction_error = None
        if modified_data is not None:
            original_hash = hash_func(input_data)
            modified_hash = hash_func(modified_data)

            original_flat = original_hash.ravel()
            modified_flat = modified_hash.ravel()

            if hash_func.__name__ == "NoHash":
                reconstruction_error = error(input_data, modified_data, metric="mae")
            else:
                reconstruction_error = error(original_flat, modified_flat)

        return {
            "time": end - start,
            "time_per_iteration": (end - start) / iterations,
            "hash_value": hash_value,
            "reconstruction_error": reconstruction_error,
        }
    except Exception as e:
        logging.error(f"Error in benchmark for {hash_func.__name__}: {str(e)}")
        return {
            "time": 0,
            "time_per_iteration": 0,
            "hash_value": None,
            "reconstruction_error": None,
            "error": str(e),
        }


def run_benchmark(image_sizes, iterations=10):
    import cv2

    results = {size: {} for size in image_sizes}
    for size in image_sizes:
        test_image = np.random.randint(0, 255, (size[0], size[1], size[2]), dtype=np.uint8)
        noise = np.random.normal(0, 5, test_image.shape).astype(np.uint8)
        modified_image = cv2.add(test_image, noise)

        for name, func in hash_methods().items():
            results[size][name] = benchmark_hash_method(func, test_image, modified_image, iterations)
    return results


def plot_results(results):
    import matplotlib.pyplot as plt

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 12))

    for size, data in results.items():
        times = [v["time_per_iteration"] for v in data.values()]
        errors = [v["reconstruction_error"] for v in data.values()]
        labels = list(data.keys())

        ax1.plot(labels, times, label=f"Time: {size[0]}x{size[1]}")
        ax2.plot(labels, errors, label=f"Reconstruction Error: {size[0]}x{size[1]}")

    ax1.set_xticks(range(len(labels)))
    ax1.set_xticklabels(labels, rotation=45)
    ax1.set_xlabel("Hash Method")
    ax1.set_ylabel("Time Per Iteration (s)")
    ax1.set_title("Hash Method Latency by Image Size")
    ax1.legend()

    ax2.set_xticks(range(len(labels)))
    ax2.set_xticklabels(labels, rotation=45)
    ax2.set_xlabel("Hash Method")
    ax2.set_ylabel("Reconstruction Error")
    ax2.set_title("Hash Method Reconstruction Error by Image Size")
    ax2.legend()

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    image_sizes = [(256, 256, 3), (512, 512, 3), (1024, 1024, 3)]
    iterations = 100

    results = run_benchmark(image_sizes, iterations)
    plot_results(results)
    from rich.pretty import pprint

    pprint(results)
