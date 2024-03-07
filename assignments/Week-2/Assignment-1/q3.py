def discount(amount: float):
    if amount <= 0:
        print("Invalid amount")
    elif amount >= 1 and amount <= 9999:
        print("You got no discount.")
    elif amount >= 10000 and amount <= 29999:
        amount -= amount * 0.1
        print("You got 10%% discount.")
    elif amount >= 30000 and amount <= 39999:
        amount -= amount * 0.2
        print("You got 20%% discount.")
    elif amount >= 40000 and amount <= 49999:
        amount -= amount * 0.25
        print("You got 25%% discount.")
    else:
        amount -= amount * 0.3
        print("You got 30%% discount.")

    print(f"Final amount: {amount:.0f}")


final_amount: float = float(input("Enter the final amount: "))
discount(final_amount)
