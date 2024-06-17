
print("Welcome to the game")
Decision = input("Do you wanna play or quit? ")
if Decision.lower() != "yes":
    print ("Looser!!!")
    quit()
else:
    print ("Game on!")
    score = 0
    answer = input("What is 1+1 ? ")
    
    if answer == "2":
        score += 1      
    else:
        score -= 1

    answer = input ("What is 2+2? ")
    if answer == "4":
        score += 1
    else:
        score -= 1
    print ("Your score is " +str(score))



