def secondLargest(my_list: list):
    largest_num = my_list[0]
    second_largest = my_list[0]

    for i in my_list:
        if i > largest_num:
            second_largest = largest_num
            largest_num = i
        elif i > second_largest and i != largest_num:
            second_largest = i
    return second_largest


my_list = [57, 26, -57, -20, 41, 79, 47, 59, -12, 77, 78]
print(secondLargest(my_list))
