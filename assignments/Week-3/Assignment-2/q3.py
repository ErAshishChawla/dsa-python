def pattern(n: int) -> None:
    for i in range(1, n + 1):
        for j in range(1, (n - i) + 1):
            print(" ", end=" ")
        for k in range(1, (2 * i - 1) + 1):
            print(i, end=" ")
        print()


pattern(5)

# Output:
"""
        1 
      2 2 2 
    3 3 3 3 3 
  4 4 4 4 4 4 4 
5 5 5 5 5 5 5 5 5 
"""
