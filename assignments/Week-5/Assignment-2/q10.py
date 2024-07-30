from typing import Dict, List


def clearLists(d: Dict[str, List[int]]) -> Dict[str, List[int]]:
    new_d = {}
    for k, v in d.items():
        new_d[k] = []

    return new_d


print(
    clearLists({"a": [1, 2, 3], "b": [4, 5, 6], "c": [7, 8, 9]})
)  # {'a': [], 'b': [], 'c': []}
