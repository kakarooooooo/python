# def user_choice():
#     choice = "First"

#     while (choice.isdigit() == False or (int(choice) > 10 or int (choice) < 0)):
#         choice = input("Please enter a number (0-10): ")

#     return int(choice)

# user_choice()


game_list = [0, 1, 2]

def display_game(game_list):
    os.system("cls")
    print ("Here is the current list: ")
    print (game_list)

def position_choice():
    choice = "First"

    while choice not in ['0','1','2']:
        choice = input ("please choose (0, 1, 2): ")

        if choice not in ['0','1','2']:
            print ("Sorry, invalid choice!")
            
    return int(choice)

def replacement_choice(game_list, position):
    user_placement = input("Type a string to place at position: ")

    game_list[position] = user_placement
    return game_list

def gameon_choice() :
    choice = "First"

    while choice not in ['Y','N']:
        choice = input ("Keep playing? (Y, N): ")

        if choice not in ['Y','N']:
            print ("Sorry, I don't understand, please choose Y or N")
            
    if choice == "Y":
        return True
    else:
        return False

game_on = True

import os

while game_on:

    display_game(game_list)

    position = position_choice()

    game_list = replacement_choice(game_list, position)

    display_game(game_list)

    game_on = gameon_choice()

