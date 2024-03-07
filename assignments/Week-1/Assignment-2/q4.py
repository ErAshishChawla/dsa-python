"""
Ask a mark from user, 0-100

91-100: A
81-90: B
71-80: C
61-70: D
0-60: F
"""

mark: float = float(input("Enter your mark = "))

if mark >= 91 and mark <= 100:
    print("A")
elif mark >= 81 and mark <= 90:
    print("B")
elif mark >= 71 and mark <= 80:
    print("C")
elif mark >= 61 and mark <= 70:
    print("D")
elif mark >= 0 and mark <= 60:
    print("F")
else:
    print("Invalid mark")
