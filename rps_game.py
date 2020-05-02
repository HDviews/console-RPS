import random

choices = ["rock", "paper", "scissors"]

def game():
    choice = random.choice(choices)
    selection = input("rock, paper, or scissors: ")
    if selection == "rock":
        if choice == choices[1]:
            print(selection, choice, "you lose!")
        elif choice == choices[0]:
            print(selection, choice, "draw!")
        else:
            print(selection, choice, "you win!")

    if selection == "paper":
        if choice == choices[2]:
            print(selection, choice, "you lose!")
        elif choice == choices[1]:
            print(selection, choice, "draw!")
        else:
            print(selection, choice, "you win!")

    if selection == "scissors":
        if choice == choices[0]:
            print(selection, choice, "you lose!")
        elif choice == choices[2]:
            print(selection, choice, "draw!")
        else:
            print(selection, choice, "you win!")
    
    selection = input("would you like to play again? yes or no?: ")
    if selection == "yes":
        game()
    else:
        exit()

game()