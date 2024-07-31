from typing import Dict


def sortDictByValues(d: Dict):
    return dict(sorted(d.items(), key=lambda x: x[1]))


print(sortDictByValues({1: 2, 3: 4, 4: 3, 2: 1, 0: 0}))
