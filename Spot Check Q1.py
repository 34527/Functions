#Euan McElhoney
#09/12/14
#Functions spot check - 1

def password_checker():
    password = password_input()
    password_validation(password)

def password_input():
    password = input("Please enter a password: ")
    passwordlength = len(password)
    return passwordlength

def password_validation(passwordlength):
    if passwordlength > 16:
        print("Password to long")
        password_checker()
    elif passwordlength < 8:
        print("password too short")
        password_checker()
    else:
        print("password accepted")


password_checker()
