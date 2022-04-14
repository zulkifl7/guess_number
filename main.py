'''
Guess number game
'''
#### There are two types of game ####

######  Type - 1  ##############
'''
Computer generates a number and user have to find the number 
* Every time computer generates a Rqndom number and user have to 
    find it.
* Every time the minimum and maximum number changed
'''
######  Type - 2  ##############
'''
User have to think of a number and Computer will find the number
**  Without existing 8 guesses **
'''




import most_used
import guess_number_cgen as cgen
import guess_number_upref as upref
def eneter_game():
    mode = input('''Select your Game mode.\nMode (1/2): ''')
    if mode == "1":
        cgen.guess_cgen()
        most_used.repfun(
            cgen.guess_cgen, is_input="Do you want to play (again)? ")
    elif mode == "2":
        upref.guess_upref()
        most_used.repfun(
            upref.guess_upref, is_input="Do you want to play (again)? ")
    else:
        print("Wrong input!")
        mode = input('''Select your Game mode.\nMode (1/2): ''')


def main():
    print('''
Guess number game
#### There are two types of game ####

######  Type - 1  ##############
Computer generates a number and user have to find the number 
* Every time computer generates a Rqndom number and user have to 
    find it.
* Every time the minimum and maximum number changed

######  Type - 2  ##############
User have to think of a number and Computer will find the number
**  Without existing 8 guesses **
    ''')

    eneter_game()
    most_used.repfun(
        eneter_game, is_input="Do you wanat to exit game? ", invert=True)


if __name__ == "__main__":
    main()
