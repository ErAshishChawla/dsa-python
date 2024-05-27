def change(a: int):
    a = 1000


a = 50
change(a)
print(a)


def display(lst: list):
    print(lst)
    print(id(lst))


my_list = [10, 20, 30]
display(my_list)
print(id(my_list))
