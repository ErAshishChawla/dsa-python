from typing import Dict


def calculateAvg(d: Dict[str, Dict[str, int]]) -> None:
    for k, v in d.items():
        total = 0
        for v1 in v.values():
            total = total + v1
        print(f"{k}: {total/len(v)}")


calculateAvg(
    {
        "John": {"Math": 85, "Science": 90, "English": 80},
        "Alice": {"Math": 75, "Science": 88, "English": 92},
        "Bob": {"Math": 90, "Science": 85, "English": 78},
    }
)
