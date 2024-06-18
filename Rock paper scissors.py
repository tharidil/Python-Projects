import random
options = ["rock", "paper", "scissors", "q"]

First_question = input("Do you wanna play Rock, Paper, Scissors? ")

if First_question.lower() not in ["yes","yo","kylla"]:
    print("Bye")
    

else:
    computer_wins = 0
    user_wins = 0
    
    while True:
        user_input = input("Rock/ Paper/ Scissors? (Press 'Q' to quit at any time.) ")
        if user_input not in options:
            print("Please check your spellings")
            continue
    
        elif user_input == "q":
            break
        
        else:
            random_number = random.randint(0,2)
            computer_input = options[random_number]
            print("The computer picked", computer_input, ".")

    
            if user_input == "rock" and computer_input == "scissors":
                user_wins += 1
                print("You won!")
                continue
            
            if user_input == "paper" and computer_input == "rock":
                user_wins += 1
                print("You won!")
                continue

            if user_input == "scissors" and computer_input == "paper":
                user_wins += 1
                print("You won!")
                continue
            if user_input == "rock" and computer_input == "rock":
                print("It is a draw!")
                continue
            
            if user_input == "paper" and computer_input == "paper":
                print("It is a draw!")
                continue

            if user_input == "scissors" and computer_input == "scissors":
                print("It is a draw!")
                continue
            else:
                print("You lost!")
                computer_wins += 1
                continue

    print("You won", user_wins, "time(s) while the computer won", computer_wins, "time(s).")
