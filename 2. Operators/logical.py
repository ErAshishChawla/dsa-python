"""
Logical Operators (To Compare 2 or more conditions)


AND : C1 and C2  ->  RESULT (True if both are True)
OR : C1 or C2  ->  RESULT (True if any one is True)
NOT: not C1  ->  RESULT (True if C1 is False, opposite of C1)
"""

physics = 16
chemistry = 20

print(physics > 15 and chemistry > 15)  # True
print(physics > 15 or chemistry > 15)  # True
print(not (physics > 15 or chemistry > 15))  # False
print(physics > 15 or not chemistry > 15)  # True

# Truthy and falsy behavior and short-circuiting
# In Python, the logical operators and and or are short-circuiting.
# This means that if the result can be determined by evaluating the first operand, the second operand is not evaluated at all.

print(46 or 0.0 or False and 0)
print(23 and 0)


print(0 or 0.0 or False and 23 or -0)
print(46 or 0.0 or False and 0)
