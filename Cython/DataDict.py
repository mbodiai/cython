

import copy
from typing import Any, Self

class DataDict(dict):
    _MISSING = object()

    def copy(self) -> Self:
        cp = type(self)()
        cp.update(self)
        return cp

    def __deepcopy__(self, memo):
        cls = type(self)
        result = cls.__new__(cls)
        memo[id(self)] = result
        dict.__init__(result)
        for key, value in self.items():
            result[key] = copy.deepcopy(value, memo)
        return result

    def __getattr__(self, name: str):
        if dict.__contains__(self, name):
            return dict.__getitem__(self, name)
        raise AttributeError(f"{self.__class__.__name__} has no attribute {name}")

    def __contains__(self, key: Any) -> bool:
        if not isinstance(key, str):
            return False
        cur = self
        while "." in key:
            head, key = key.split(".", 1)
            if not dict.__contains__(cur, head):
                return False
            cur = dict.__getitem__(cur, head)
            if not isinstance(cur, dict):
                return False
        return dict.__contains__(cur, key) or key in getattr(type(self), "__dataclass_fields__", [])

    def __setattr__(self, name: str, value: Any) -> None:
        if name in getattr(type(self), "__dataclass_fields__", []):
            object.__setattr__(self, name, value)
            dict.__setitem__(self, name, value)
        else:
            object.__setattr__(self, name, value)

    def __getitem__(self, key: str) -> Any:
        cur = self
        while "." in key:
            head, key = key.split(".", 1)
            if not dict.__contains__(cur, head):
                raise KeyError(head)
            next_val = dict.__getitem__(cur, head)
            if not isinstance(next_val, dict):
                raise KeyError(key)
            cur = next_val
        if dict.__contains__(cur, key):
            val = dict.__getitem__(cur, key)
            # If retrieving a group without a subkey, expose its 'enabled' if present
            if isinstance(val, dict) and "enabled" in val:
                return val["enabled"]
            return val
        raise KeyError(key)

    def __setitem__(self, key: str, value: Any) -> None:
        # Support dotted assignment into nested mappings
        if "." in key:
            head, tail = key.split(".", 1)
            # Use raw dict containment to avoid DataDict.__contains__ semantics here
            if dict.__contains__(self, head) and isinstance(dict.__getitem__(self, head), dict):
                dict.__getitem__(self, head)[tail] = value
                return
        # If setting a group value and it has an 'enabled' toggle, store there
        if dict.__contains__(self, key):
            cur_val = dict.__getitem__(self, key)
            if isinstance(cur_val, dict) and "enabled" in cur_val and not isinstance(value, dict):
                cur_val["enabled"] = value
                if key in getattr(type(self), "__dataclass_fields__", []):
                    object.__setattr__(self, key, cur_val)
                return
        # Prefer dataclass field assignment for local fields
        if key in getattr(type(self), "__dataclass_fields__", []):
            object.__setattr__(self, key, value)
            dict.__setitem__(self, key, value)
            return
        dict.__setitem__(self, key, value)

    def __delattr__(self, name: str) -> None:
        if dict.__contains__(self, name):
            dict.__delitem__(self, name)
        object.__delattr__(self, name)

    def __delitem__(self, key: str) -> None:
        if dict.__contains__(self, key):
            dict.__delitem__(self, key)
        else:
            object.__delattr__(self, key)

    def dict(self) -> dict[str, Any]:
        return type(self)(**self)

    def get(self, key: str, default: Any = None) -> Any:
        try:
            return self[key]
        except KeyError:
            value = self._get_field_default(key)
            if value is self._MISSING:
                return default
            return value

    def _get_field_default(self, key: str) -> Any:
        cur: Any = self
        remaining = key
        while True:
            fields = getattr(type(cur), "__dataclass_fields__", {})
            if "." in remaining:
                head, remaining = remaining.split(".", 1)
                if head not in fields:
                    return self._MISSING
                cur = getattr(cur, head)
                if not isinstance(cur, DataDict):
                    return self._MISSING
                continue
            if remaining in fields:
                return getattr(cur, remaining)
            return self._MISSING
