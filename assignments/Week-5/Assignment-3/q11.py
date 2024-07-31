from typing import Dict


def sortByKeysLenInAsc(d: Dict):
    return dict(sorted(d.items(), key=lambda x: len(x[0])))


print(
    sortByKeysLenInAsc(dict([("apple", 2), ("banana", 3), ("pear", 4), ("orange", 5)]))
)
