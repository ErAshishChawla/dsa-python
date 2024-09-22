from typing import Dict


def sortDict(d: Dict[str, int]):
    return dict(sorted(d.items(), key=lambda x: x[1], reverse=True))


my_dict = {"a": 100, "b": 200, "c": 300}
print(sortDict(my_dict))
