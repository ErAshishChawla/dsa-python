from typing import Dict


def checkEmptyDict(d: Dict) -> bool:
    # keys = d.keys()

    # return len(keys) == 0
    return not d


print(checkEmptyDict({}))
print(checkEmptyDict({"": 1}))
