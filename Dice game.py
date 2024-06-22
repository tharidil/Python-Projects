import random

#def roll():
    


while True:
    players = input("How many players? (2-4): ")
    if players.isdigit():
        players=int(players)
        if 2<=players<=6:
            current_score=0
            max_score=50
    
            while True:
                Game_play=input("Would you like to roll the dice? (y/n): ")
                if Game_play.lower== "y":
                    value=roll()

                    if value!= 1:
                        current_score += value
                        if current_score==max_score:
                            break
                    else:
                        print("You rolled a",value,"!")
                        current_score = 0
                        print("You got a score of",current_score)
                        break
                elif Game_play.lower== "n":
                    quit()
                else:
                    print("Enter a valid answer")
                    
                
        else:
            print("Number of players should be 2 to 4")    
    else:
        Print("Please enter a valid number")
        continue
    
    '''current_score=0
    max_score=50
    
    while True:
        Game_play=input("Would you like to roll the dice? (y/n): ")
        if Game_play.lower==("y"):
            roll = random.randint(1,6)
            print("You got ",roll,"!")

            if roll!=(1):
                current_score = current_score+roll
                if current_score==max_score:
                    break
            else:
                current_score = 0
        elif Game_play.lower==("n"):
            quit()
        else:
            Print("Enter a valid answer")
            
        print("You got",current_score)
        break'''
        

