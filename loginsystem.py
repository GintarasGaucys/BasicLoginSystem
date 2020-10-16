
def isdone():
    answer = input("Do you want to exit? Y/N   ")
    if answer.lower() == "y":
        return True
    if answer.lower() == "n":
        return False



def addinfo(mail, password):
    database = open("database.txt", "a")
    infostr = mail + " " + password + "\n"
    database.write(infostr)
    database.close()


def isalreadyregistered(mail):
    database = open("database.txt", "r")
    datalist = database.readlines()
    for i in datalist:
        ilist = i.split()
        if ilist[0] == mail:
            database.close()
            return True
    database.close()
    return False


def checkpassword(mail, password):
    database = open("database.txt", "r")
    datalist = database.readlines()
    for i in datalist:
        ilist = i.split()
        if ilist[0] == mail.strip():
            if ilist[1] == password:
                database.close()
                return True
    database.close()
    return False

done = False
while not done:
    answer = input("Do you want to login or register? L/R  ")
    if answer.lower() == "l":
        mail = input("Enter your email: ")
        if isalreadyregistered(mail) == True:
            password = input("Please enter your password: ")
            if checkpassword(mail, password) == True:
                print("Password correct. You have logged in.")
                done = isdone()
            else:
                print("Password incorrect.")
                done = isdone()
        else:
            print("Email not found, please register.")
            done = isdone()
    elif answer.lower() == "r":
        mail = input("Enter your email (1 word): ")
        password = input("Enter your password (1 word): ")
        passwordcheck = input("Enter your password again: ")
        if isalreadyregistered(mail):
            print("Email already registered.")
            done = isdone()
        elif password == passwordcheck:
            addinfo(mail, password)
            print("Succesfully registered")
            done = isdone()
        else:
            print("Passwords dont match")
            done = isdone()
    else:
        print("Input not recognized.")
        done = isdone()
        if done == True:
            break

