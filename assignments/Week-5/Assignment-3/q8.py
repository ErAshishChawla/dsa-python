from typing import Dict


def reverseDict(d: Dict) -> Dict:
    reversed_dict = {}
    for k, v in d.items():
        reversed_dict[v] = k
    return reversed_dict


print(reverseDict({1: 2, 3: 4, 4: 3, 2: 1, 0: 0}))
