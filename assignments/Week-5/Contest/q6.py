from typing import List, Dict


def dictListToInt(dictList: List[Dict[str, str]]) -> List[Dict[str, int]]:
    new_list = list()

    for i in dictList:
        new_dict = dict()
        for k, v in i.items():
            new_dict[k] = int(v)
        new_list.append(new_dict)

    return new_list


def dictListToFloat(dictList: List[Dict[str, str]]) -> List[Dict[str, float]]:
    new_list = list()

    for i in dictList:
        new_dict = dict()
        for k, v in i.items():
            new_dict[k] = float(v)
        new_list.append(new_dict)

    return new_list


def converValues(dictList: List[Dict[str, str]]) -> List[Dict]:
    new_list = list()

    for i in dictList:
        new_dict = dict()
        for k, v in i.items():
            if "." in v:
                new_dict[k] = float(v)
            else:
                new_dict[k] = int(v)
        new_list.append(new_dict)

    return new_list


print(
    converValues([{"x": "10", "y": "20", "z": "30"}, {"p": "40", "q": "50", "r": "60"}])
)
print(
    converValues(
        [
            {"x": "10.12", "y": "20.23", "z": "30"},
            {"p": "40.00", "q": "50.19", "r": "60.99"},
        ]
    )
)
