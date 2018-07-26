

decision = raw_input("Would you like to roll the dice? Yes/No ")

if decision == "No":
    print("Thank you for playing.")
    exit()

if decision != "No" and decision != "Yes":
    print("That answer was insufficient. Would you like to roll the dice? Yes/No")
    decision = raw_input("Would you like to roll the dice? Yes/No ")
