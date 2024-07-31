from typing import Dict, List


def printDictLineByLine(d: Dict[str, Dict[str, int]]) -> None:
    for k, v in d.items():
        print(k)
        for k1, v1 in v.items():
            print(f"{k1} : {v1}")


printDictLineByLine(
    {
        "Sam": {"M1": 89, "M2": 56, "M3": 89},
        "Suresh": {"M1": 49, "M2": 96, "M3": 89},
    }
)
