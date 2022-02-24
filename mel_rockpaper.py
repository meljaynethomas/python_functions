# ROCK - 0
# PAPER - 1
# SCISSORS - 2

import random

# create another function to get player input, and another to get computer input
# can then implement a while loop to keep looping until player inputs correct information....

print("ROCK...PAPER...SCISSORS!")
print("Can you beat the computer?")
player = input("Enter R for Rock, P for Paper, and S for Scissors: ")
if player == "R":
    player = 0
    print(f"Your choice is: Rock")
elif player == "P":
    player = 1
    print(f"Your choice is: Paper")
elif player == "S":
    player = 2
    print(f"Your choice is: Scissors")
else:
    print("You have entered an incorrect character. Please try again!")


computer = random.randint(0, 2)
if computer == 0:
    print(f"Computer chooses: Rock")
if computer == 1:
    print(f"Computer chooses: Paper")
if computer == 2:
    print(f"Computer chooses: Rock")


def compare_values(player, computer):
    if player == 0 and computer == 0:
        print("It's a draw!")
    if player == 1 and computer == 1:
        print("It's a draw!")
    if player == 2 and computer == 2:
        print("It's a draw!")
    if player == 0 and computer == 1:
        print("Paper Wraps Rock - Computer Wins!")
    if player == 0 and computer == 2:
        print("Rock Smashes Scissors - Player Wins!")
    if player == 1 and computer == 0:
        print("Paper Wraps Rock - Player Wins!")
    if player == 1 and computer == 2:
        print("Scissors Cut Paper - Computer Wins!")
    if player == 2 and computer == 0:
        print("Rock Smashes Scissors - Computer Wins!")
    if player == 2 and computer == 1:
        print("Scissors Cut Paper - Player Wins!")


compare_values(player, computer)
