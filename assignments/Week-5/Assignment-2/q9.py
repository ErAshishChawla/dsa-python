from typing import Dict


def removeGreaterThanK(d: Dict[str, int], k1: int) -> Dict[str, int]:
    new_d = {}
    for k, v in d.items():
        if v <= k1:
            new_d[k] = v

    return new_d


print(removeGreaterThanK({"a": 1, "b": 2, "c": 3}, 2))  # {'a': 1, 'b': 2}
print(removeGreaterThanK({"a": 1, "b": 2, "c": 3}, 1))  # {'a': 1}
