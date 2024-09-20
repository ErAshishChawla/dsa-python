"""
Make a class named area

There are no attributes related to area
It should have 4 methods
1. rectangle
l,b -> input

2. square
s-> input

3. circle
r->parameter

4. triangle
b,h->parameter
"""

import math


class Area:
    def rectangle(self):
        l = float(input("Enter length: "))
        b = float(input("Enter breadth: "))
        area = l * b

        print("Area of rectangle: ", area)

    def square(self):
        s = float(input("Enter side: "))
        area = s * s

        print("Area of square: ", area)

    def circle(self, r=0):
        area = math.pi * r * r
        print("Area of circle: ", area)

    def triangle(self, b=0, h=0):
        area = 0.5 * b * h
        print("Area of triangle: ", area)


a = Area()
a.rectangle()
