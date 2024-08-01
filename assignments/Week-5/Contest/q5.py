from typing import List, Dict


def mergeListsToDict(list1: List, list2: List) -> Dict:
    if len(list1) != len(list2):
        return dict()

    merged_dict = dict()
    for i in range(len(list1)):
        merged_dict[list1[i]] = list2[i]

    return merged_dict


print(mergeListsToDict([1, 2, 3], ["a", "b", "c"]))
