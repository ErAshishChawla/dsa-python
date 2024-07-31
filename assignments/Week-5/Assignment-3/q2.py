from typing import Dict, List


def countItems(d: Dict[str, List]) -> int:
    count = 0
    for k, v in d.items():
        count = count + len(v)
    return count


print(countItems({"M1": [1, 2, 3, 4, 4], "M2": [4, 5, 6], "M3": [7, 8]}))
