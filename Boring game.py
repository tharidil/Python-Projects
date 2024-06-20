name = input("Please enter your name: ")
print("Welcome",name,"to the boring game.")

q1 = input("You are going to go to bed. It is 9 pm. Would you set an alarm? (yes/no): ").lower()
if q1 == "yes":
    q11 =input("What is the time you set the alarm? (5am/6am/7am) ").lower()
    if q11 == "5am":
        print("You woke up axactly at 5 am.")
        q111 = input("What would you use first? (washroom/coffee/phone)").lower()
        if q111 == "washroom":
