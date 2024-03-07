angle_1: int = int(input("Enter the first angle: "))
angle_2: int = int(input("Enter the second angle: "))
angle_3: int = int(input("Enter the third angle: "))

if angle_1 + angle_2 + angle_3 != 180:
    print("The angles do not form a triangle")
else:
    if angle_1 == 90 or angle_2 == 90 or angle_3 == 90:
        print("The triangle is a right-angled triangle")
    elif angle_1 > 90 or angle_2 > 90 or angle_3 > 90:
        print("The triangle is an obtuse-angled triangle")
    else:
        print("The triangle is an acute-angled triangle")
