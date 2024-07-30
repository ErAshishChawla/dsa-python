from typing import Dict, List


def func(d: Dict[str, List]) -> List:
    values = []

    for l in d.values():
        for i in l:
            values.append(i)

    return values


print(func({"a": [1, 2, 3], "b": [4, 5, 6], "c": [7, 8, 9]}))
