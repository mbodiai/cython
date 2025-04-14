"""Interfaces for accessing metadata.

We provide two implementations.
 * The "classic" file system implementation, which uses a directory
   structure of files.
 * A hokey sqlite backed implementation, which basically simulates
   the file system in an effort to work around poor file system performance
   on OS X.

Object Storage Format
-------------------
Complex objects are stored using a custom serialization format that preserves
type information for proper reconstruction. The format handles:

* Nested dataclasses
* Lists and sequences
* Dictionaries
* Primitive types

Examples
--------
Given these dataclasses:

    @dataclass
    class Address:
        street: str
        city: str

    @dataclass
    class Person:
        name: str
        addresses: List[Address]
        metadata: Dict[str, str]

The serialized format would look like:

    {
        '__dataclass__': 'Person',
        'module': 'your_module',
        'data': {
            'name': 'John Doe',
            'addresses': [
                {
                    '__dataclass__': 'Address',
                    'module': 'your_module',
                    'data': {
                        'street': '123 Main St',
                        'city': 'NYC'
                    }
                }
            ],
            'metadata': {'id': '12345'}
        }
    }

Usage Example
------------
    store = FilesystemMetadataStore("/cache/path")

    # Writing
    person = Person(
        name="John Doe",
        addresses=[Address("123 Main St", "NYC")],
        metadata={"id": "12345"}
    )
    store.write_object("person.data", person)

    # Reading
    loaded_person = store.read_object("person.data", Person)
"""

from __future__ import annotations

import binascii
import os
import time
from abc import abstractmethod
from typing import TYPE_CHECKING, Any, Iterable, List, TypeVar, Type
from dataclasses import is_dataclass, fields
import pickle

if TYPE_CHECKING:
    # We avoid importing sqlite3 unless we are using it so we can mostly work
    # on semi-broken pythons that are missing it.
    import sqlite3

T = TypeVar("T")


class MetadataStore:
    """Generic interface for metadata storage with object serialization support.

    This class provides methods for storing and retrieving complex object structures
    while preserving their type information and relationships. It handles:

    * Dataclass instances with nested fields
    * Lists and sequences of objects
    * Dictionaries with arbitrary value types
    * Primitive types (int, str, float, etc.)

    The serialization process traverses the entire object graph and creates a
    type-aware representation that can be accurately reconstructed later.
    """

    @abstractmethod
    def getmtime(self, name: str) -> float:
        """Read the mtime of a metadata entry.

        Raises FileNotFound if the entry does not exist.
        """

    @abstractmethod
    def read(self, name: str) -> bytes:
        """Read the contents of a metadata entry.

        Raises FileNotFound if the entry does not exist.
        """

    @abstractmethod
    def write(self, name: str, data: bytes, mtime: float | None = None) -> bool:
        """Write a metadata entry.

        If mtime is specified, set it as the mtime of the entry. Otherwise,
        the current time is used.

        Returns True if the entry is successfully written, False otherwise.
        """

    @abstractmethod
    def remove(self, name: str) -> None:
        """Delete a metadata entry."""

    @abstractmethod
    def commit(self) -> None:
        """If the backing store requires a commit, do it.

        But N.B. that this is not *guaranteed* to do anything, and
        there is no guarantee that changes are not made until it is
        called.
        """

    @abstractmethod
    def list_all(self) -> Iterable[str]: ...

    def serialize_object(self, obj: Any) -> bytes:
        """Serialize an object including its nested structure.

        Args:
            obj: Any Python object to serialize (dataclass, list, dict, etc.)

        Returns:
            bytes: Serialized representation of the object

        Example:
            address = Address("123 Main St", "NYC")
            data = store.serialize_object(address)
        """
        return pickle.dumps(self._prepare_object(obj))

    def deserialize_object(self, data: bytes, cls: Type[T]) -> T:
        """Deserialize an object and reconstruct its structure.

        Args:
            data: Previously serialized bytes
            cls: The expected type to reconstruct

        Returns:
            An instance of cls with all nested structures restored

        Raises:
            TypeError: If the serialized data doesn't match the expected type

        Example:
            data = store.read("person.data")
            person = store.deserialize_object(data, Person)
        """
        raw_data = pickle.loads(data)
        return self._reconstruct_object(raw_data, cls)

    def _prepare_object(self, obj: Any) -> Any:
        """Recursively prepare an object for serialization."""
        if is_dataclass(obj):
            return {
                "__dataclass__": obj.__class__.__name__,
                "module": obj.__class__.__module__,
                "data": {
                    f.name: self._prepare_object(getattr(obj, f.name))
                    for f in fields(obj)
                },
            }
        elif isinstance(obj, (list, tuple)):
            return [self._prepare_object(item) for item in obj]
        elif isinstance(obj, dict):
            return {k: self._prepare_object(v) for k, v in obj.items()}
        return obj

    def _reconstruct_object(self, data: Any, expected_type: Type[T]) -> T:
        """Recursively reconstruct an object from serialized data."""
        if isinstance(data, dict) and "__dataclass__" in data:
            if (
                data["module"] != expected_type.__module__
                or data["__dataclass__"] != expected_type.__name__
            ):
                raise TypeError(
                    f"Expected {expected_type.__name__}, got {data['__dataclass__']}"
                )

            field_values = {}
            for f in fields(expected_type):
                field_type = f.type
                field_data = data["data"][f.name]
                field_values[f.name] = self._reconstruct_object(field_data, field_type)
            return expected_type(**field_values)

        elif isinstance(data, list):
            if hasattr(expected_type, "__origin__") and expected_type.__origin__ in (
                list,
                List,
            ):
                item_type = expected_type.__args__[0]
                return [self._reconstruct_object(item, item_type) for item in data]
            return data

        return data

    def write_object(self, name: str, obj: Any, mtime: float | None = None) -> bool:
        """Write an object to the store, handling nested structures."""
        data = self.serialize_object(obj)
        return self.write(name, data, mtime)

    def read_object(self, name: str, cls: Type[T]) -> T:
        """Read and reconstruct an object from the store."""
        data = self.read(name)
        return self.deserialize_object(data, cls)


def random_string() -> str:
    return binascii.hexlify(os.urandom(8)).decode("ascii")


class FilesystemMetadataStore(MetadataStore):
    def __init__(self, cache_dir_prefix: str) -> None:
        # We check startswith instead of equality because the version
        # will have already been appended by the time the cache dir is
        # passed here.
        if cache_dir_prefix.startswith(os.devnull):
            self.cache_dir_prefix = None
        else:
            self.cache_dir_prefix = cache_dir_prefix

    def getmtime(self, name: str) -> float:
        if not self.cache_dir_prefix:
            raise FileNotFoundError()

        return int(os.path.getmtime(os.path.join(self.cache_dir_prefix, name)))

    def read(self, name: str) -> bytes:
        assert os.path.normpath(name) != os.path.abspath(name), (
            "Don't use absolute paths!"
        )

        if not self.cache_dir_prefix:
            raise FileNotFoundError()

        with open(os.path.join(self.cache_dir_prefix, name), "rb") as f:
            return f.read()

    def write(self, name: str, data: bytes, mtime: float | None = None) -> bool:
        assert os.path.normpath(name) != os.path.abspath(name), (
            "Don't use absolute paths!"
        )

        if not self.cache_dir_prefix:
            return False

        path = os.path.join(self.cache_dir_prefix, name)
        tmp_filename = path + "." + random_string()
        try:
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(tmp_filename, "wb") as f:
                f.write(data)
            os.replace(tmp_filename, path)
            if mtime is not None:
                os.utime(path, times=(mtime, mtime))

        except OSError:
            return False
        return True

    def remove(self, name: str) -> None:
        if not self.cache_dir_prefix:
            raise FileNotFoundError()

        os.remove(os.path.join(self.cache_dir_prefix, name))

    def commit(self) -> None:
        pass

    def list_all(self) -> Iterable[str]:
        if not self.cache_dir_prefix:
            return

        for dir, _, files in os.walk(self.cache_dir_prefix):
            dir = os.path.relpath(dir, self.cache_dir_prefix)
            for file in files:
                yield os.path.normpath(os.path.join(dir, file))


SCHEMA = """
CREATE TABLE IF NOT EXISTS files2 (
    path TEXT UNIQUE NOT NULL,
    mtime REAL,
    data BLOB
);
CREATE INDEX IF NOT EXISTS path_idx on files2(path);
"""


def connect_db(db_file: str) -> sqlite3.Connection:
    import sqlite3.dbapi2

    db = sqlite3.dbapi2.connect(db_file)
    db.executescript(SCHEMA)
    return db


class SqliteMetadataStore(MetadataStore):
    def __init__(self, cache_dir_prefix: str) -> None:
        # We check startswith instead of equality because the version
        # will have already been appended by the time the cache dir is
        # passed here.
        if cache_dir_prefix.startswith(os.devnull):
            self.db = None
            return

        os.makedirs(cache_dir_prefix, exist_ok=True)
        self.db = connect_db(os.path.join(cache_dir_prefix, "cache.db"))

    def _query(self, name: str, field: str) -> Any:
        # Raises FileNotFound for consistency with the file system version
        if not self.db:
            raise FileNotFoundError()

        cur = self.db.execute(f"SELECT {field} FROM files2 WHERE path = ?", (name,))
        results = cur.fetchall()
        if not results:
            raise FileNotFoundError()
        assert len(results) == 1
        return results[0][0]

    def getmtime(self, name: str) -> float:
        mtime = self._query(name, "mtime")
        assert isinstance(mtime, float)
        return mtime

    def read(self, name: str) -> bytes:
        data = self._query(name, "data")
        assert isinstance(data, bytes)
        return data

    def write(self, name: str, data: bytes, mtime: float | None = None) -> bool:
        import sqlite3

        if not self.db:
            return False
        try:
            if mtime is None:
                mtime = time.time()
            self.db.execute(
                "INSERT OR REPLACE INTO files2(path, mtime, data) VALUES(?, ?, ?)",
                (name, mtime, data),
            )
        except sqlite3.OperationalError:
            return False
        return True

    def remove(self, name: str) -> None:
        if not self.db:
            raise FileNotFoundError()

        self.db.execute("DELETE FROM files2 WHERE path = ?", (name,))

    def commit(self) -> None:
        if self.db:
            self.db.commit()

    def list_all(self) -> Iterable[str]:
        if self.db:
            for row in self.db.execute("SELECT path FROM files2"):
                yield row[0]
