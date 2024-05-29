"""
* * * *
 * * * *
  * * * *
   * * * *
    * * * *
"""


def pattern(n: int) -> None:
    spaces_count = 0
    for i in range(1, n + 1):
        for j in range(1, spaces_count + 1):
            print(" ", end="")
        for k in range(1, (n - 1) + 1):
            print("*", end=" ")
        spaces_count = spaces_count + 1
        print()


pattern(5)
