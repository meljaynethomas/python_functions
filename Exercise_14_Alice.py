# defined functions
# ATTEMPT at using  keyword parameters
# def convert_user_input (**rps):
#     argsdict = dict(R='Rock', P='Paper', S='Scissors')


# creating function to convert user input - 'R', 'P' or 'S' - into 'Rock', 'Paper' or 'Scissors'
def convert_user_input(user_input_letter):
    if user_input_letter == 'R':
        user_selection = 'Rock'
    elif user_input_letter == 'P':
        user_selection = 'Paper'
    else:
        user_selection = 'Scissors'
    return user_selection


# creating a function to generate a random number between 0 and 2
def generate_random_number_0_to_2():
    import random
    random_number = random.randint(0, 2)
    return random_number


# creating function to convert computer number - 0, 1, or 2 - into 'Rock', 'Paper' or 'Scissors'
def convert_computer_number(computer):
    if computer_number == 0:
        computer_selection = 'Rock'
    elif computer_number == 1:
        computer_selection = 'Paper'
    else:
        computer_selection = 'Scissors'
    return computer_selection


# creating a function to determine win, loss or draw:
def determine_game_outcome(user, computer):
    if converted_user_input == converted_computer_word:
        outcome = 'D'
    elif converted_user_input == 'Rock' and converted_computer_word == 'Scissors':
        outcome = 'W'
    elif converted_user_input == 'Rock' and converted_computer_word == 'Paper':
        outcome = 'L'
    elif converted_user_input == 'Paper' and converted_computer_word == 'Rock':
        outcome = 'W'
    elif converted_user_input == 'Paper' and converted_computer_word == 'Scissors':
        outcome = 'L'
    elif converted_user_input == 'Scissors' and converted_computer_word == 'Paper':
        outcome = 'W'
    else:
        outcome = 'L'
    return outcome


# STEP 1 - user input: R, P, or S
accepted_user_inputs = ['R', 'P', 'S']

# REVISIT: couldn't figure out how to use upper method to ensure entry is not case-sensitive
# REVISIT: can't get this while loop to work without printing error message

user_input = None

while user_input not in accepted_user_inputs:
    user_input = input('Please enter R, P, or S: ')
    # print('You have not entered an accepted letter, please try again.')

# STEP 2 - convert user input to 'Rock', 'Paper' or 'Scissors'
converted_user_input = convert_user_input(user_input)
print('You have selected: ', converted_user_input)

# STEP 3 - generate random number between 0 and 2:
computer_number = generate_random_number_0_to_2()

# STEP 4 - convert computer number to string to compare to user selection:
converted_computer_word = convert_computer_number(computer_number)
print('Computer has selected: ', converted_computer_word)

# STEP 4 - compare user input and computer number to determine outcome of game:

game_outcome = determine_game_outcome(converted_user_input, converted_computer_word)

win_message = "You win!"
lose_message = "You lose!"
draw_message = "You draw!"

if game_outcome == 'W':
    print(win_message)
elif game_outcome == 'L':
    print(lose_message)
else:
    print(draw_message)

# thoughts: could you write a shorter script which compares the user and computer selections as integers rather than converting the random number into string?







