# The goal: Simulate rolling dice. The program will randomly choose a number between 1 and 6. The program will then print what that number is. Then ask the user if they'd like to roll again.


def get_number():
    from random import randint
    print(randint(1, 6))


# idea for refactor: use while loops instead of conditional logic? 

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
