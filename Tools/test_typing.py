from typing import List, Dict, Optional

def add_numbers(a: int, b: float) -> float:
    return a + b

class Point:
    x: float
    y: float
    
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
        
    def distance(self, other: "Point") -> float:
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5

def process_items(items: List[int], mapping: Dict[str, float]) -> Optional[float]:
    total: float = 0.0
    for item in items:
        if str(item) in mapping:
            total += mapping[str(item)]
    return total if total > 0 else None
