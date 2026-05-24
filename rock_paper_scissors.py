from random import randrange
from random import seed
from datetime import datetime
from pprint import pprint

# This is the rock-papaer-scissors game.
# The user picks a number 1, 2 or 3, according to the preffered choice
# Computer picks a number 0, 1 or 2 randomly.
# The two choices compared to each other and the winner of each round is printed
# The game ends after 3 rounds

choices = ["rock", "paper", "scissors"]

rounds = {}

# rounds = {
#     "r": [{
#         "player": "",
#         "computer": "",
#
#     }],
#     "score": ""
# }

seed(str(datetime.now()))

# Uses those two to declare the winner
c_count = 0
u_count = 0
round_count = 0

while c_count < 3 and u_count < 3:
    index = randrange(0, 3)

    computer = choices[index]

    user = int(input("Pick a number. 1: rock, 2: paper, 3: scissors: "))

    users_choice = choices[user - 1]

    # checks the winner of the current round
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

    round_count += 1
    rounds["Round" + str(round_count)] = [{"Player": users_choice, "Computer": computer, "Score": str(u_count) + ":" + str(c_count) }]


# Prints the winner of the game
if u_count == 3:
    print("THE WINNER IS: USER")
else:
    print("THE WINNER IS COMPUTER")

pprint(rounds)
