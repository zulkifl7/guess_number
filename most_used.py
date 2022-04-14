'''
This is a Module for oporations which i use in many cases
** Module is under Building Stage **
'''

######  Function -1  ##############
'''
repfun(function , string, integer)

atiributes
----------
func -> the function to be repeated
in_input -> If this is a Function which has to be repeated unitl user says no
             then the String Question shoukd be included
n_times -> if the function need to be repeated several times
            then the int should be given
'''


def repfun(func, is_input=None, n_times=None, invert=False):
    if is_input != None:
        if invert == True:
            m = 1
            continue_q = input(f"{is_input}").upper()
            while m == 1:
                # if user say yes it will run the the function
                if continue_q == "N" or continue_q == "NO":
                    func()
                    continue_q = input(f"{is_input}").upper()
                # if the use wants to stop he can say no and stop
                elif continue_q == "Y" or continue_q == "YES":
                    break
                # for invalid inputs Question will be repeated
                else:
                    print('''Invalid Input!\nEnter Yes or No''')
                    continue_q = input(f"{is_input}").upper()
        if invert == False:
            m = 1
            continue_q = input(f"{is_input}").upper()
            while m == 1:
                # if user say yes it will run the the function
                if continue_q == "Y" or continue_q == "YES":
                    func()
                    continue_q = input(f"{is_input}").upper()
                # if the use wants to stop he can say no and stop
                elif continue_q == "N" or continue_q == "NO":
                    break
                # for invalid inputs Question will be repeated
                else:
                    print('''Invalid Input!\nEnter Yes or No''')
                    continue_q = input(f"{is_input}").upper()
    elif n_times != None:
        if type(n_times) == int:
            m = 0
            while m < n_times:
                func()
    else:
        print("Exact repeating method is not mentioned")
