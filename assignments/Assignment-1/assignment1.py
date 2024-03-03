# Q1

print("-------------------------------Q1---------------------------------")
a = 5
b = 10

print(a > 5 and b >= 10)  # False
print(a >= 5 or not b > 10)  # True
print(not (a > 5 and b > 5))  # True
print(not (a < 10 or not b < 10))  # False
print(not (not a <= 5 or not b >= 10))  # True


# Q2
print("-------------------------------Q2---------------------------------")

kms = float(input("Enter the distance in kilometers: "))  # We convert it to float
miles = kms * 0.621371
print(f"{kms} kilometers is equal to {miles} miles")


# Q3
print("-------------------------------Q3---------------------------------")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

average = (num1 + num2 + num3) / 3
print(f"The average of {num1}, {num2} and {num3} is {average}")
print(f"The average of {num1}, {num2} and {num3} is {average:.2f}")

# Q4
print("-------------------------------Q4---------------------------------")

rupees = int(input("Enter the amount in rupees: "))
paise = rupees * 100
print(f"{rupees} rupees is equal to {paise} paise")

# Q5
print("-------------------------------Q5---------------------------------")

side = float(input("Enter the length of the side of the square: "))
area = side**2

print(f"The area of the square with side {side} is {area}")
print(f"The area of the square with side {side} is {area:.2f}")

# Q6
print("-------------------------------Q6---------------------------------")

total_games = int(input("Enter the total number of games played: "))
won = int(input("Enter the number of games won: "))
lost = int(input("Enter the number of games lost: "))

tie = total_games - (won + lost)

tie_points = tie * 2
won_points = won * 4
total_points = tie_points + won_points

print(f"{total_points = }")
print(f"{tie = }")


# Q7
print("-------------------------------Q7---------------------------------")

input_num = int(input("Enter a number: "))
if (input_num % 3) == 0:
    print("The number is divisible by 3")
else:
    print("The number is not divisible by 3")


# Q8
print("-------------------------------Q8---------------------------------")

input_num = int(input("Enter a number: "))
if (input_num % 2) == 0:
    print("The number is even")
else:
    print("The number is odd")

# Q9
print("-------------------------------Q9---------------------------------")

length = float(input("Enter the length of the rectangle: "))
breadth = float(input("Enter the breadth of the rectangle: "))

if length == breadth:
    print("The rectangle is a square")
else:
    print("The rectangle is not a square")
