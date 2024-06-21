master_pwd = input("Please enter the master password: ")

def view():
    with open("passwords1.txt","r") as f:
        for line in f.readlines():
            data=line.rstrip()
            user, passw = data.split("|")
            print("User:", user,"Password:", passw)
                    
def add():
    user_name=input("User name: ")
    pwd=input("Password: ")

    with open("passwords1.txt","a") as f:
        f.write(user_name +"|" +pwd+'\n')
    
while True:
    mode = input("Would you like to add a new password or view an existing one? (view/add) :")
    if mode == "q":
        break
    elif mode == "add":
        add()
    elif mode == "view":
        view()
    else:
        print("Invalid mode.")
        continue
        

