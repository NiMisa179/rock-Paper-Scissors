from random import randrange
from random import seed
from datetime import datetime

choices = ["rock", "paper", "scissors"]

seed(str(datetime.now()))
index = randrange(0, 3)

computer = choices[index]
user = int(input("Pick a number. 1: rock, 2: paper, 3: scissors: "))

users_choice = choices[user - 1]

if (users_choice == "rock" and computer == "paper") or (
        users_choice == "scissors" and computer == "rock") or (
    users_choice == "paper" and computer == "scissors"
):
    print("Computer had", computer)
    print("Computer wins")
elif (users_choice == "paper" and computer == "rock") or (
        users_choice == "rock" and computer == "scissors") or (
    users_choice == "paper" and computer == "scissors"
):
    print("Computer had", computer)
    print("User wins")
else:
    print("TIE")