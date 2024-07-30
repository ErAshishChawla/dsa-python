from typing import Dict, List


def mergeLists(dict1: Dict[str, int], dict2: Dict[str, int]) -> Dict[str, int]:
    new_dict = {}

    for k, v in dict1.items():
        total = 0
        if k in dict2.keys():
            total = v + dict2[k]

        new_dict[k] = total
    return new_dict


print(mergeLists({"a": 1, "b": 2}, {"a": 3, "b": 4}))  # {'a': 4, 'b': 6}
