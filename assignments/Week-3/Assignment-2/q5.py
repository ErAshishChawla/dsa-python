def pattern(n: int) -> None:
    top_half_rows = n // 2 + 1
    bottom_half_rows = n - top_half_rows
    for i in range(1, top_half_rows + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

    for i in range(bottom_half_rows, 0, -1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()


pattern(9)

# Output:
"""
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 
1 2 3 4 
1 2 3 
1 2 
1 
"""
