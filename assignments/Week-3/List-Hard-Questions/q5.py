def displayCount(my_list: list) -> None:
    checked = []

    highest_count = 0
    highest_count_value = 0

    print()

    for i in my_list:
        if i not in checked:
            element_count = my_list.count(i)
            print(f"{i} : {element_count} times")
            checked.append(i)

            if element_count > highest_count:
                highest_count = element_count
                highest_count_value = i
    print(
        f"The element with the highest occurence is : {highest_count_value} ({highest_count} times)"
    )


my_list = [54, 14, 11, 12, 54, 14, 14, 11, 54, 11, 11, 11]

displayCount(my_list)
