def twoListsToDict(l1: list, l2: list) -> dict:
    if len(l1) != len(l2):
        return {"error": "Lists are not of equal length"}

    new_dict = {}
    for i in range(len(l1)):
        new_dict[l1[i]] = l2[i]

    return new_dict


print(twoListsToDict([1, 2, 3], ["a", "b", "c"]))
