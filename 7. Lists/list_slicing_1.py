my_list = [45, 31, 76, 54, [11, 32, 100]]

result = my_list[0 : len(my_list)]

print(id(my_list[4]))
print(id(result[4]))

print(my_list)
print(result)
