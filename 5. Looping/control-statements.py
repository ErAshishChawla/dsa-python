# BREAK, CONTINUE

i: int = 1

while i <= 10:
    if i == 5:
        break
    print(i, end=" ")
    i += 1
print()


i: int = 1
while i <= 10:
    print(i, end=" ")
    i += 1
    if i == 5:
        break
print()

i: int = 1
while i <= 10:
    i += 1
    if i == 5:
        continue
    print(i, end=" ")
    print("Done", end=" ")
print()

# i: int = 1
# while i <= 10:
#     print(i, end=" ")
#     if i == 5:
#         continue
#     i += 1
# infinite loop as the value of i will reach 5 and then never will be incremented
print()

i: int = 1
while i <= 10:
    print(i, end=" ")
    i += 1
    if i == 5:
        continue
print()
