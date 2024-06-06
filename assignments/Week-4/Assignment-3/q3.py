def checkElementInTuple(tup, ele):
    if ele in tup:
        return True
    return False


tup = (1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 6, 7, 8, 9)

num = int(input("Enter a number to check in the tuple: "))

print(checkElementInTuple(tup, num))
