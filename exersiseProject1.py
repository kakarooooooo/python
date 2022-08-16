import os

def display_game(game_list):
    os.system("cls")
    print(game_list[7] + "|" + game_list[8] + "|" + game_list[9])
    print(game_list[4] + "|" + game_list[5] + "|" + game_list[6])
    print(game_list[1] + "|" + game_list[2] + "|" + game_list[3])

def position_choice():
    while 1:
        choice = input("Player 1: Do you want to be X or O?: ").upper()
        if choice in ['X', 'O']:
            if (choice == 'X'):
                print ("Player 1 will go first")
                return ('X', 'O')
            else:
                print ("Player 2 will go first")
                return ('O', 'X')
        else:
            print("Sorry, please choose X or O")

def ready_check():
    check = "First"
    while True:
        check = input("Are you ready to play? Enter Yes or No ").lower()
        if check in ['yes', 'no']:
            break
        else:
            print ("Sorry, I don't understand, please choose Yes or No")
    
    if check == 'yes':
        return True
    else:
        return False

def choose_position(game_array, sign):
    choice = "First"
    while True:
        choice = input("Choose your next position (1-9): ")
        if choice.isdigit == False or int(choice) not in range(1,10):
            print ("Please enter number in (1-9)")
        elif choice.isdigit and not (game_array[int(choice)] == " "):
            print ("Already selected number. Please select again.")
        else:
            break
    game_array[int(choice)] = sign
    return game_array

def check_win(game_array):
    return False

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

sample_list = ["sample", "7", "8", "9", "4", "5", "6", "1", "2", "3"]
display_game(sample_list)
game_on = True

while game_on:
    game_list = ["game"," "," "," "," "," "," "," "," "," "]
    player1_marker, player2_marker = position_choice()
    ready_check()
    end_game = False
    display_game(sample_list)
    game_list = choose_position(game_list, "X")
    display_game(game_list)

    while not end_game:
        game_list = choose_position(game_list, "O")
        end_game = check_win(game_list)
        display_game(game_list)

        if end_game:
            break
        game_list = choose_position(game_list, "X")
        end_game = check_win(game_list)
        display_game(game_list)

    game_on = gameon_choice()

