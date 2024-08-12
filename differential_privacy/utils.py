from typing import List


def sensitivity(data: List[float]) -> float:
    return max(data) - min(data)
