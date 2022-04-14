# Computer generated

from random import randint


def guess_cgen():
    # generating the maximum and minimum number which is in between 1 to 999
    min_num = randint(1, 1000)
    max_num = randint(1, 1000)
    while (min_num > max_num) or 100 < (max_num - min_num) or (max_num - min_num) < 50:
        max_num = randint(1, 1000)
    # generating the exact random number for the game
    random_num = randint(min_num, max_num)
    guess_log = {}

    # user guessing starts
    count = 1
    big_or_small = None
    guess = int(input(
        f"Enter your guess from {min_num} to {max_num} [Guess number {count}]: "))

    print()
    # looping while the answer is not ncorrect
    while guess != random_num:
        # checking if the number is in the range
        if min_num < guess < max_num:
            # looking the guess is bigger or smaller than the answer
            # and instructing user accordingly
            if guess > random_num:
                print("Your guess is bigger than the number!!")
                big_or_small = "Big"
            elif guess < random_num:
                print("Your guess is smaller than the number!!")
                big_or_small = "Small"
        else:
            print("Your guess is outof range!!")

        # adding the user entered value and value status into the guess_log
        guess_log[str(count)] = [guess, big_or_small]
        # displaying use's previos guesses and status
        for num in guess_log.keys():
            print(
                f"[Guess number {num} => {guess_log[num][0]} ({guess_log[num][1]})]")
        count += 1
        guess = int(input(f"Enter your guess [Guess number {count}]: "))
    print(f"Correct answer!!! The number was {random_num}")
