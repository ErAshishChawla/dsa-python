"""
3 requirements to get a certificate:
1. Part of C&D
2. Minimum class attendance is 20
3. Minimum assignment submitted = 45

Are you a part of CD? (yes/no)
yes && Enter class attendance : >20
yes &7  Enter assignment submitted: >45
yes && "You will get certificate"

no && "Cannot get ceritificate
"""

part_of_cd: str = input("Are you a part of C&D? (yes/no): ").lower()

output_message: str = ""

if part_of_cd == "yes":
    class_attendance: int = int(input("Enter class attendance: "))
    if class_attendance >= 20:
        assignment_submitted: int = int(input("Enter assignment submitted: "))
        if assignment_submitted >= 45:
            output_message = "You will get certificate"
        else:
            output_message = "Cannot get certificate"
    else:
        output_message = "Cannot get certificate"

elif part_of_cd == "no":
    output_message = "Cannot get certificate"
else:
    output_message = "Invalid input"

print(output_message)
