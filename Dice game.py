import random

def roll():
    min=1
    max=6
    roll=random.randint(min,max)
    return roll

while True:
    players = input("How many players? (2-4): ")
    if players.isdigit():
        players=int(players)
        if 2<=players<=4:
            break            
        else:
            print("Number of players should be 2 to 4")    
    else:
        print("Please enter a valid number")
        continue
 
max_score=20
player_scores=[0 for i in range(players)]
print(player_scores)

    
while max(player_scores) < max_score:
    for player_index in range(players):
        print("Turn of player",player_index+1)
        print("Your currrent score is", player_scores[player_index])

        while True:
            Game_play=input("Would you like to roll the dice? (y/n): ")
            if Game_play.lower() == 'y':
                value=roll()

                if value!= 1:
                    player_scores[player_index] += value
                    print("You rolled a",value,"!")
                    print("Current score: ",player_scores[player_index])                 
                                    
                else:
                    print("You rolled a",value,"!")
                    player_scores[player_index] = 0
                    print("Next player please. Your new score: ",player_scores[player_index])
                    break
                
            elif Game_play.lower() == "n":
                break
            else:
                print("Enter a valid answer")
        
print("Player",player_index+1,"won !!!")
