import random
import time

U = 12
L = 3
ope = ["+","-","*"]
Total = 5

def pproblem():
    left = random.randint(L, U)
    right = random.randint(L, U)
    OPE = random.choice(ope)

    expr = str(left) + " " + OPE + " " + str(right)
    ans = eval(expr)
    return expr, ans

input("Press any key to start")
print("------------")
ST = time.time()
wrong =0
for i in range(Total):
    expr, ans = pproblem()
    while True:
        guess=input("Problem " + str(i + 1) + ": "+ expr +" = ")
        if guess == str(ans):
            break
        wrong+=1
ET=time.time()
time_taken=round(ET-ST,2)
print("Time taken is "+str(time_taken)+', while you got it wrong '+str(wrong)+' times.' )


