final_amount: float = float(input("Enter the final amount: "))


if final_amount <= 0:
    print("Invalid amount")
elif final_amount >= 1 and final_amount <= 9999:
    print("You got no discount.")
elif final_amount >= 10000 and final_amount <= 29999:
    final_amount -= final_amount * 0.1
    print("You got 10%% discount.")
elif final_amount >= 30000 and final_amount <= 39999:
    final_amount -= final_amount * 0.2
    print("You got 20%% discount.")
elif final_amount >= 40000 and final_amount <= 49999:
    final_amount -= final_amount * 0.25
    print("You got 25%% discount.")
else:
    final_amount -= final_amount * 0.3
    print("You got 30%% discount.")

print(f"Final amount: {final_amount:.0f}")
