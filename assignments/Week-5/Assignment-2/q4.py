from typing import Dict, List


def mergeLists(dict1: Dict[str, List], dict2: Dict[str, List]) -> Dict[str, List]:
    new_dict = {}

    for k, v in dict1.items():
        new_values = []
        if k in dict2.keys():
            for i in v:
                new_values.append(i)
            for i in dict2[k]:
                new_values.append(i)
        new_dict[k] = new_values

    return new_dict


print(
    mergeLists({"a": [1, 2, 3], "b": [4, 5, 6]}, {"a": [7, 8, 9], "b": [10, 11, 12]})
)  # {'a': [1, 2, 3, 7, 8, 9], 'b': [4, 5, 6, 10, 11, 12]}
