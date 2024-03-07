classes_held: int = int(input("Enter the number of classes held: "))
classes_attended: int = int(input("Enter the number of classes attended: "))

if (
    classes_held < classes_attended
    or classes_held < 0
    or classes_attended < 0
    or classes_held == 0
):
    print("Invalid input")
else:
    attendance_percentage: float = (classes_attended / classes_held) * 100

    print(f"Attendance percentage: {attendance_percentage:.2f}%")

    if attendance_percentage >= 0 and attendance_percentage < 75:
        print("You are not allowed to sit in the exam")
    elif attendance_percentage >= 75 and attendance_percentage <= 100:
        print("You are allowed to sit in the exam")
    else:
        print("Invalid input")
