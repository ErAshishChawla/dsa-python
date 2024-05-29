my_list = [i for i in range(1, 11)]
print(my_list)

my_list = [1 for i in range(1, 11)]
print(my_list)

my_list = [i % 2 for i in range(1, 11)]
print(my_list)

my_list = [i for i in range(-10, -1, -1)]
print(my_list)

my_list = [i for i in range(10, -1, -1)]
print(my_list)


my_list = [i % 2 == 0 for i in range(1, 11)]
print(my_list)
