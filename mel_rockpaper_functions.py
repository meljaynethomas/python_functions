import random


def get_player_input():
    player_choice = input("Enter R for Rock, P for Paper, and S for Scissors: ").upper()
    return_val = -1
    if player_choice == "R":
        print(f"Your Choice Is: Rock")
        return_val = 0
    elif player_choice == "P":
        print(f"Your Choice Is: Paper")
        return_val = 1
    elif player_choice == "S":
        print(f"Your Choice Is: Scissors")
        return_val = 2
    return return_val


def get_computer_input():
    computer_choice = random.randint(0, 2)
    if computer_choice == 0:
        print(f"Computer Chooses: Rock")
    elif computer_choice == 1:
        print(f"Computer Chooses: Paper")
    elif computer_choice == 2:
        print(f"Computer Chooses: Scissors")
    return computer_choice


def compare_values(player_selection, computer_selection):
    if player_selection == computer_selection:
        return "It's a draw!"
    elif player_selection == 0 and computer_selection == 1:
        return "Paper Wraps Rock - Computer Wins!"
    elif player_selection == 0 and computer_selection == 2:
        return "Rock Smashes Scissors - Player Wins!"
    elif player_selection == 1 and computer_selection == 0:
        return "Paper Wraps Rock - Player Wins!"
    elif player_selection == 1 and computer_selection == 2:
        return "Scissors Cut Paper - Computer Wins!"
    elif player_selection == 2 and computer_selection == 0:
        return "Rock Smashes Scissors - Computer Wins!"
    elif player_selection == 2 and computer_selection == 1:
        return "Scissors Cut Paper - Player Wins!"



def main():
    player_selection = -1
    while player_selection < 0:
        player_selection = get_player_input()

    computer_selection = get_computer_input()
    game_outcome = compare_values(player_selection, computer_selection)
    print(game_outcome)


if __name__ == "__main__":
    main()