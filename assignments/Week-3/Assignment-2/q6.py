def pattern(n: int) -> None:
    top_half_rows = n // 2 + 1
    bottom_half_rows = n - top_half_rows
    for i in range(top_half_rows, 0, -1):
        for j in range(i, top_half_rows + 1):
            print(j, end=" ")
        print()

    for i in range(1, bottom_half_rows + 1):
        for j in range(i + 1, bottom_half_rows + 1 + 1):
            print(j, end=" ")
        print()


pattern(9)

# Output:
"""
5 
4 5 
3 4 5 
2 3 4 5 
1 2 3 4 5 
2 3 4 5 
3 4 5 
4 5 
5
"""
