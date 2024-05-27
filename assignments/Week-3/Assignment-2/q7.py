def pattern(n: int) -> None:
    top_half_rows = n // 2 + 1
    bottom_half_rows = n - top_half_rows
    for i in range(1, top_half_rows + 1):
        for j in range(1, top_half_rows - i + 1):
            print(" ", end=" ")
        for k in range(1, (2 * i - 1) + 1):
            print(k, end=" ")
        print()

    for i in range(bottom_half_rows, 0, -1):
        for j in range(1, (bottom_half_rows + 1 - i) + 1):
            print(" ", end=" ")
        for k in range(1, (2 * i - 1) + 1):
            print(k, end=" ")
        print()


pattern(9)

# Output:
"""
        1 
      1 2 3 
    1 2 3 4 5 
  1 2 3 4 5 6 7 
1 2 3 4 5 6 7 8 9 
  1 2 3 4 5 6 7 
    1 2 3 4 5 
      1 2 3 
        1 
"""
