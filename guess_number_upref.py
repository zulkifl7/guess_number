# User preference

from random import randint


def guess_upref():
    # generating the maximum and minimum number which is in between 1 to 999
    min_num = randint(1, 1000)
    max_num = randint(1, 1000)
    while (min_num > max_num) or (max_num - min_num) != 50:
        max_num = randint(1, 1000)
    # generating the exact random number for the game
    print(f"Take a number from {min_num} to {max_num}.")
    input("Press ENTER when you are done!")

    count = 1
    guess_log = {}

    last_type = ""
    guess = (max_num + min_num)//2
    print(f"Guess {count} => {guess}")
    print('''C -> Correct\nB -> Computer's Guess is Bigger than the number\nS -> Computer's Guess is Smaller than the number''')
    check = input("Is that correct? ").upper()

    while check != "C":
        if check == "B":
            max_num = guess
            guess_log[f"{count}"] = [min_num, max_num]
            last_type == "B"
        elif check == "S":
            min_num = guess
            guess_log[f"{count}"] = [min_num, max_num]
            last_type == "S"
        else:
            print("Wrong input!!")
            check = input("Is that correct? ").upper()
            continue

        # Excemption for missing numbers
        '''last number and the first number may sometimes get ignored because 
            in puthon answer for a devision is a float'''
        if guess == (max_num + min_num)//2:
            if last_type == "B":
                guess -= 2
            elif last_type == "S":
                guess += 2
        else:
            count += 1
            guess = (max_num + min_num)//2
            print(f"\nGuess {count} => {guess}")
            print('''C -> Correct\nB -> Computer's Guess is Bigger than the number\nS -> Computer's Guess is Smaller than the number''')
            check = input("Is that correct? ").upper()
