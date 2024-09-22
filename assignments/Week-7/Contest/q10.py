from typing import Dict


def sumOfItemsInDict(d: Dict[str, int]) -> int:
    # Write your code here
    return sum(d.values())


my_dict = {"a": 100, "b": 200, "c": 300}
print(sumOfItemsInDict(my_dict))  # 600
