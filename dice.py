def get_number():
    from random import randint
    print(randint(1, 6))




def roll_dice():
    decision = raw_input("Would you like to roll the dice? yes/no ").strip()

    if decision == "yes" or decision == "Yes":
        get_number()
        roll_dice()

    if decision == "no" or decision == "No":
        print("Thank you for playing.")
        exit()

    if decision != "no" and decision != "yes":
        print("That answer was insufficient.")
        roll_dice()


roll_dice()
