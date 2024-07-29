from typing import Dict


def dictLength(d: Dict) -> int:
    return len(d)


print(dictLength({}))
print(dictLength({"": 1}))
