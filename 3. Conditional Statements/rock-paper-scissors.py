""""
Rock Paper Scissors

Rock paper scissors is a classic two player game. Each player chooses either rock, paper, or scissors. The possible outcomes are:

    Rock destroys scissors.
    Scissors cut paper.
    Paper covers rock.
    If there’s a tie, then the game ends in a draw.

computer_choice = rock/paper/scissors(random choice on program start)

user_choice = input("Enter rock, paper, or scissors: ") if user_choice is not rock, paper, or scissors, print "Invalid choice"

if
elif
elif ...


You won
You lost, the computer chose
you tied
"""

import random

options: list = ["rock", "paper", "scissors"]

computer_choice: str = random.choice(options)

user_choice: str = input("Enter rock, paper, or scissors: ").lower()

if user_choice != "rock" and user_choice != "paper" and user_choice != "scissors":
    print("Invalid choice")
elif user_choice == "rock" and computer_choice == "scissors":
    print("You won")
elif user_choice == "paper" and computer_choice == "rock":
    print("You won")
elif user_choice == "scissors" and computer_choice == "paper":
    print("You won")
elif computer_choice == user_choice:
    print("You tied")
else:
    print(f"You lost, the computer chose {computer_choice}")
