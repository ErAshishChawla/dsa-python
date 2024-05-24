"""
print 1 to 10 using for loop
"""

for i in range(1, 11):
    print(i, end=" ")
print()

start: int = int(input("Enter the start number: "))
end: int = int(input("Enter the end number: "))

total: int = 0

for i in range(start, end + 1):
    print(i, end=" ")
    total += i
print()
print(f"Total of numbers from {start} to {end} is {total}")

# print the following pattern
for i in range(1, 11, 2):
    print(i, end=" ")


end = 11
# Print 10 to 1
for i in range(10, end + 1):
    print(i, end=" ")
    end += 1
