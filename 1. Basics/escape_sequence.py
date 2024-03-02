# Escape Sequence

"""
Escape Sequence

- Always used inside strings ("" or '')

\n -> New Line
\t -> Tab
\\ -> Backslash
\" -> Double Quote
\' -> Single Quote
\b -> Backspace
\r -> Carriage Return
"""

print("Hello\t\tWorld\n Good Bye")

print("My name is Ashish\nMy age is 25\nMy gender is male")

# output : My name is A\Chawla
print("My name is A\\Chawla")

# output : My name is "Ashish"
print('My name is "Ashish"')

# output : a"\\"xyz'"\
print('a"\\\\"xyz\'"\\')
