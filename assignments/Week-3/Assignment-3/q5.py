def countOddEven(lst: list):
    odd = 0
    even = 0
    for i in lst:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1
    print(f"Total even numbers = {even}")
    print(f"Total odd numbers = {odd}")


my_list = [34, 11, 91, 59, 33, 22]

countOddEven(my_list)
