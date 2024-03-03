"""
Type Conversion / Type Casting
To convert form one data type to another data type
"""

print("Type Conversion / Type Casting")
print("-----------------------------")
print("str to int")
print("Value inside the string must be proper integer")
a = "100 "
b = "200"
print(int(a) + int(b))

print("-----------------------------")
print("str to float")
print("Value inside the string must be proper float or proper integer")
print(
    "If value is a proper integer inside the string, it will be converted to float and .0 will be appended"
)
a = float("100")
b = float(" 200")

print(a + b)

print("-----------------------------")
print("int to float")
a = 100
print(float(a))

print("-----------------------------")
print("float to int")
print(
    "Value will be rounded off to the nearest integer towards zero, basically the decimal part will be removed"
)
a = 100.99
print(int(a))
b = -10.01
print(int(b))

print("-----------------------------")
print("int to bool")
a = bool(-555)
print(a)
b = bool(-0)
print(b)

print("-----------------------------")
print("float to bool")
a = bool(-555.55)
print(a)
b = bool(-0.0)
print(b)

print("-----------------------------")
print("str to bool")
a = bool("Hello")
print(a)
b = bool("")
print(b)
