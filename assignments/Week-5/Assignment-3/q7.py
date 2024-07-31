from typing import Dict


def getDifferenceInTwoDicts(d1: Dict, d2: Dict) -> None:
    dict1_uniques = [k for k in d1.keys() if k not in d2.keys()]
    dict2_uniques = [k for k in d2.keys() if k not in d1.keys()]
    common_keys = [k for k in d1.keys() if k in d2.keys()]

    print(f"Unique keys in dict1: {dict1_uniques}")
    print(f"Unique keys in dict2: {dict2_uniques}")
    print(f"Common keys: {common_keys}")


getDifferenceInTwoDicts({"a": 1, "b": 2, "c": 3}, {"b": 2, "c": 4, "d": 5})
