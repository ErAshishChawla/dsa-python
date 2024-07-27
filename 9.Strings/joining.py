"""
String -> List
List -> String
"""

my_string = "Hello, World!"
my_list = list(my_string)
print(my_list)

my_list = [1, 2, 3, 4, 5]
my_string = str(my_list)  # Wrong Way
print(my_string)  # Output: [1, 2, 3, 4, 5] #Wrong Way
print(my_string[0])

# Joining :
my_list = [1, 2, 3, 4, 5]
my_string = "".join([str(i) for i in my_list])
print(my_string)  # Output: 1 2 3 4 5
