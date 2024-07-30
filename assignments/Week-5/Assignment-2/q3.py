from typing import List, Dict


def func(d: Dict[str, List[int]]) -> Dict[str, List[int]]:
    new_d = {}

    for k, v in d.items():
        even_values = []
        for i in v:
            if i % 2 == 0:
                even_values.append(i)
        new_d[k] = even_values

    return new_d


print(
    func({"a": [1, 2, 3], "b": [4, 5, 6], "c": [7, 8, 9]})
)  # {'a': [2], 'b': [4, 6], 'c': [8]}
