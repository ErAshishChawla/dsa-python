"""
Ask a number from user.

if div by 3 print foo
if div by 5 print bar
if div by 3 and 5 print foobar
else print foofoobarbar
"""

number: int = int(input("Enter a number= "))

if number % 3 == 0 and number % 5 == 0:
    print("foobar")
elif number % 3 == 0:
    print("foo")
elif number % 5 == 0:
    print("bar")
else:
    print("foofoobarbar")
