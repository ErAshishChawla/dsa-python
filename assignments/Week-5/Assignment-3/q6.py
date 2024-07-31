from typing import Dict
import math


def getMaxAndMin(d: Dict) -> tuple:
    max_value = float("-inf")
    min_value = float("inf")

    for v in d.values():
        if v > max_value:
            max_value = v
        if v < min_value:
            min_value = v
    return (max_value, min_value)


print(getMaxAndMin({1: 2, 3: 4, 4: 3, 2: 1, 0: 0}))
