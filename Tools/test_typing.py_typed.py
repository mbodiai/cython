import cython
from typing import List, Dict, Optional


@cython.locals(a='long', b='double')
def add_numbers(a: int, b: float) -> float:
    return a + b

class Point:
    x: float
    y: float
    
    @cython.locals(x='double', y='double')
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
        
    @cython.locals(other='object')
    def distance(self, other: "Point") -> float:
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5

@cython.locals(items='list', mapping='dict')
def process_items(items: List[int], mapping: Dict[str, float]) -> Optional[float]:
    total: float = 0.0
    for item in items:
        if str(item) in mapping:
            total += mapping[str(item)]
    return total if total > 0 else None



__cy_typed__ = True
__cy_meta__ = {
    "version": 1,
    "module_name": "test_typing",
    "module_path": "test_typing.py",
    "module_hash": "9f7c8c9a6d3c4e6b",
    "compiled_at": "2021-09-28T15:25:29.000000",
    "dependencies": {
        "cython": "0.29.24"
    }
}

