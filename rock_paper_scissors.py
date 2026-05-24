from random import randrange
from random import seed
from datetime import datetime

choices = ["rock", "paper", "scissors"]

seed(str(datetime.now()))

c_count = 0
u_count = 0

while c_count < 3 and u_count < 3:
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
        c_count += 1
    elif (users_choice == "paper" and computer == "rock") or (
            users_choice == "rock" and computer == "scissors") or (
            users_choice == "paper" and computer == "scissors"
    ):
        print("Computer had", computer)
        print("User wins")
        u_count += 1
    else:
        print("TIE")

if u_count == 3:
    print("THE WINNER IS: USER")
else:
    print("THE WINNER IS COMPUTER")
