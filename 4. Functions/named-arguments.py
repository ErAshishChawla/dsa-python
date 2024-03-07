def totalMarks(physics: int, chemistry: int, maths: int, english: int, computer: int):
    total = physics + chemistry + maths + english + computer
    print(f"Total Marks= {total}")


totalMarks(chemistry=96, computer=100, english=90, maths=95, physics=98)
# totalMarks(physics=98, 96,95, english=90, computer=100) # SyntaxError: positional argument follows keyword argument
