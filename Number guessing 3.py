import random

def guess(x):
    random_number=random.randint(1,x)
    guess=0
    while int(guess)!= random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_number:
            print("Try a higher one.")
        elif guess > random_number:
            print("Try a lower one")
        else:            
            print(f"You guessed it correctly ")
            break

guess(5)
