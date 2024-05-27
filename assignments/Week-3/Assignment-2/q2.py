def pattern(n: int) -> None:
    for i in range(1, n + 1):
        for j in range(1, (n - i) + 1):
            print(" ", end=" ")
        for k in range(n, n - i, -1):
            print(k, end=" ")
        print()


pattern(5)

# Output:
"""
        5 
      5 4 
    5 4 3 
  5 4 3 2 
5 4 3 2 1 
"""
