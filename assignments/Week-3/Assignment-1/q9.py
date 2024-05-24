start = 1
for i in range(1, 6):
    for j in range(start, start + i):
        print(j, end=" ")
        start = j + 1
    print()

# Another solution:
"""
First lets print the pattern normally then we will think about numbers
now we are basically counting and printing that count. For each inner loop we are printing the count instead of the loop variable and incrementing the count by 1
"""
count = 1
for i in range(1, 6):
    for j in range(1, i + 1):
        print(count, end=" ")
        count = count + 1
    print()

# Output:
"""
1 
2 3 
4 5 6 
7 8 9 10 
11 12 13 14 15 
"""
