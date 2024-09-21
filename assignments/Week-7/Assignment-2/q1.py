class Student:
    def __init__(self):
        self.name = input("Enter the name of the student: ").title()
        self.age = int(input("Enter the age of the student: "))
        self.gender = input("Enter the gender of the student: ").title()
        self.marks = []
        for i in range(5):
            self.marks.append(float(input(f"Enter the marks of subject {i + 1}: ")))

    def displayAllInfo(self):
        print(f"\nName: {self.name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")
        print(f"Marks: {self.marks}\n")

    def displayOnlyMarks(self):
        print(f"\nMarks: {self.marks}\n")

    def getTotal(self):
        return sum(self.marks)

    def getMax(self):
        return max(self.marks)

    def getMin(self):
        return min(self.marks)

    def getAvg(self):
        return sum(self.marks) / len(self.marks)

    def addMark(self, mark):
        self.marks.append(mark)

    def removeMark(self):
        self.marks.pop()


student1 = Student()

student1.displayAllInfo()

student1.displayOnlyMarks()

print(f"Total Marks: {student1.getTotal()}")

print(f"Maximum Marks: {student1.getMax()}")

print(f"Minimum Marks: {student1.getMin()}")

print(f"Average Marks: {student1.getAvg()}")

student1.addMark(105)
student1.displayOnlyMarks()

student1.removeMark()
student1.displayAllInfo()
