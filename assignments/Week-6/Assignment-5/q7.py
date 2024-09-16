def tupleListToDict(t):
    res_dict = dict()
    for k, v in t:
        res_dict[k] = [v]

    return res_dict


ip = [("a", 1), ("b", 2), ("c", 3)]
print(tupleListToDict(ip))
