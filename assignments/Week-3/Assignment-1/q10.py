for i in range(5, 0, -1):
    for j in range(1, i + 1):
        if j % 2 == 0:
            print(2, end=" ")
        else:
            print(1, end=" ")
    print()

# Output:
"""
1 2 1 2 1 
1 2 1 2 
1 2 1 
1 2 
1 

"""
