def sumCountOddEven(lst: list):
    even_sum = 0
    odd_sum = 0
    for i in lst:
        if i % 2 == 0:
            even_sum = even_sum + i
        else:
            odd_sum = odd_sum + i
    print(f"Even numbers sum = {even_sum}")
    print(f"Odd numbers sum = {odd_sum}")


my_list = [34, 11, 91, 59, 33, 22]

sumCountOddEven(my_list)
