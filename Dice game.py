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
            print("Number of players should be 2 to 4.")    
    else:
        print("Please enter a valid number")
        continue
 
max_score=20
player_scores=[0 for i in range(players)]
print(player_scores)

    
while max(player_scores) < max_score:
    for player_index in range(players):
        print("Turn of player",player_index+1)
        print("Your currrent score is", player_scores[player_index],".")
        current_score=0
        while True:
            Game_play=input("Would you like to roll the dice? (y/n): ")
            if Game_play.lower() == 'n':
                break
            if Game_play.lower() != 'y':
                print("Next player please. You turned down the turn.")
                break
            value=roll()

            if value == 1:
                current_score -= value
                print("You rolled a",value,"! and the current score is ",current_score,".")
                print("Next player please.")
                break                 
                                    
            else:
                print("You rolled a",value,"!")
                current_score += value
            print( "Your score as of now: ",current_score)

        player_scores[player_index]+=current_score  
        #print("Your total score is", player_scores[player_index],".")    
                
        
            
print("Player",player_index+1,"won with a score of",str(max(player_scores))," !!!")
