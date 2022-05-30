from random import shuffle

def shuffle_list(mylist):
    shuffle(mylist)
    return mylist

def player_guess():
    guess = ''
    while guess not in ['0', '1', '2']:
        guess = input("Enter your number: 0,1, or 2: ")
    return (int(guess))

def check_guess(mylist,guess):
    if mylist[guess] == 'O':
        return True
    else:
        return False
        
mylist = [' ', 'O', ' ']

result = shuffle_list(mylist)

myindex = player_guess()

if check_guess(result, myindex):
    print("true")
else:
    print("false")
    print(result)


# https://docs.google.com/document/d/181AMuP-V5VnSorl_q7p6BYd8mwXWBnsZY_sSPA8trfc/edit?usp=sharing