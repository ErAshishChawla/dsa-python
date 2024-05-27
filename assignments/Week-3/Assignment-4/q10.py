user_list = []

for i in range(1, 11):
    num = int(input(f"Enter number {i}: "))
    user_list.append(num)

print("Original List:", user_list)

only_odds = []

for i in user_list:
    if i % 2 != 0:
        only_odds.append(i)

print("List with only odd numbers:", only_odds)
