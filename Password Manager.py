master_pwd = input("Please enter the master password: ")

def view():
    pass


def add():
    user_name=input("User name: ")
    pwd=input("Password: ")

    with open("passwords.txt","a") as f:
        f.write(user_name+"|"+pwd+'\n')
    
while True:
    mode = input("Would you like to add a new password or view an existing one? (view/add) :")
    if mode == "q":
        break
    if mode == "add":
        add()
    if mode == "view":
        view()
    else:
        print("Invalid mode.")
        continue
        

