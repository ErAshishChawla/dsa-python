def checkTriangle(a: int | float, b: int | float, c: int | float) -> None:
    if a == b == c:
        print("Equilateral Triangle")
    elif a == b or b == c or c == a:
        print("Isosceles Triangle")
    else:
        print("Scalene Triangle")


checkTriangle(3, 3, 3)
checkTriangle(3, 3, 4)
checkTriangle(3, 4, 5)
