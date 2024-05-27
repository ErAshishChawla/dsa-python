user_list = []

for i in range(1, 11):
    num = int(input(f"Enter number {i}: "))
    user_list.append(num)

print("Original List:", user_list)

# Dont do this in interview
# copiedList = user_list.copy()
# copiedList.reverse()

reversed_list = []

for i in range(len(user_list) - 1, -1, -1):
    reversed_list.append(user_list[i])

print("Reversed List:", reversed_list)
