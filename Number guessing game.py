import random

random_number = random.randint(0,10)
guesses = 0
while True:
    user_guess = input("Guess a number between 0 & 10 ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
        guesses += 1
    else:
        print ("Please type a viable number ")
    if user_guess == random_number:
            print ("You got it in", guesses,"guesses.")
            quit()
    elif user_guess < random_number:
        print("Try a number higher than the guess")
    else:
        print("Try again")
