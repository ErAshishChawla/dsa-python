from typing import Dict


def sortByKeysInAsc(d: Dict):
    return dict(sorted(d.items(), key=lambda x: x[0]))


print(sortByKeysInAsc({"b": 2, "a": 1, "c": 3}))
