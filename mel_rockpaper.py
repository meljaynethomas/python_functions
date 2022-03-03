import random


def compare_values(player_choice, computer_choice):
    if player_choice == computer_choice:
        print("It's a draw!")
    if player_choice == 0 and computer_choice == 1:
        print("Paper Wraps Rock - Computer Wins!")
    if player_choice == 0 and computer_choice == 2:
        print("Rock Smashes Scissors - Player Wins!")
    if player_choice == 1 and computer_choice == 0:
        print("Paper Wraps Rock - Player Wins!")
    if player_choice == 1 and computer_choice == 2:
        print("Scissors Cut Paper - Computer Wins!")
    if player_choice == 2 and computer_choice == 0:
        print("Rock Smashes Scissors - Computer Wins!")
    if player_choice == 2 and computer_choice == 1:
        print("Scissors Cut Paper - Player Wins!")


print("ROCK...PAPER...SCISSORS!")
print("Can You Beat The Computer?")

while True:

    player_input = ""
    accepted_player_inputs = ['R', 'P', 'S']

    while player_input not in accepted_player_inputs:
        player_input = input("Enter R for Rock, P for Paper, and S for Scissors: ").upper()

    if player_input == "R":
        player_input = 0
        print(f"Your Choice Is: Rock")
    elif player_input == "P":
        player_input = 1
        print(f"Your Choice Is: Paper")
    elif player_input == "S":
        player_input = 2
        print(f"Your Choice Is: Scissors")

    computer_input = random.randint(0, 2)
    if computer_input == 0:
        print(f"Computer Chooses: Rock")
    elif computer_input == 1:
        print(f"Computer Chooses: Paper")
    elif computer_input == 2:
        print(f"Computer Chooses: Scissors")

    compare_values(player_input, computer_input)

    play_again = input("Would You Like To Play Again? Y/N: ").upper()
    if play_again == "N":
        break





