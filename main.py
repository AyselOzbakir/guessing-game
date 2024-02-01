import random

def guess(x):
    random_number = random.randint(1, x)
    user_guess = 0
    while user_guess != random_number:
        user_guess = int(input(f"Guess a number between 1 and {x}: "))
        if user_guess < random_number:
            print("Sorry, wrong guess. Too low!")
        elif user_guess > random_number:
            print("Sorry, wrong guess. Too high!")

    print(f"Congratulations! You have guessed the number {random_number} correctly!")

def player_guess(x):
    low = 1
    high = x
    feedback = ""
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low

        feedback = input(f"Is {guess} too high (H), too low (L), or correct (C)? ").lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
        else:
            print(f"Great! The player guessed your number, {guess}, correctly.")
guess(10)
player_guess(10)
