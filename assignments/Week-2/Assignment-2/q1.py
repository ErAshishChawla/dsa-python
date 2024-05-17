# def largest(
#     num1: int | None = None, num2: int | None = None, num3: int | None = None
# ) -> int:
#     if num1 is None:
#         if num2 is None:
#             if num3 is None:
#                 return -1
#             return num3
#         elif num3 is None:
#             if num2 is None:
#                 return -1
#             return num2
#         return num2 if num2 > num3 else num3

#     elif num2 is None:
#         if num3 is None:
#             return num1
#         return num1 if num1 > num3 else num3

#     elif num3 is None:
#         return num1 if num1 > num2 else num2
#     else:
#         largest: int = num1
#         if num2 > largest:
#             largest = num2
#         if num3 > largest:
#             largest = num3
#         return largest


def largest(
    num1: float | None = None, num2: float | None = None, num3: float | None = None
) -> float:
    if num1 != None and num2 != None and num3 != None:
        largest: float = num1
        if num2 > largest:
            largest = num2
        elif num3 > largest:
            largest = num3
        return largest
    return -1


print(largest())
