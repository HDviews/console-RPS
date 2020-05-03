import random
import os

choices = ["rock", "paper", "scissors"]
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

os.system("Pause")