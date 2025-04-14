import string
from typing import Any

from tomlkit._utils import escape_string
from tomlkit.items import Key, KeyType


class SingleKey(Key):
    """A single key."""

    def __init__(
        self,
        k: str | Any,
        t: KeyType | None = None,
        sep: str | None = None,
        original: str | None = None,
    ) -> None:
        # Convert non-string keys to string
        k = str(k) if not isinstance(k, str) else k

        if t is None:
            if not k or any(
                c not in string.ascii_letters + string.digits + "-" + "_" for c in k
            ):
                t = KeyType.Basic
            else:
                t = KeyType.Bare

        self.t = t
        if sep is None:
            sep = " = "

        self.sep = sep
        self.key = k
        if original is None:
            key_str = escape_string(k) if t == KeyType.Basic else k
            original = f"{t.value}{key_str}{t.value}"

        self._original = original
        self._keys = [self]
        self._dotted = False
