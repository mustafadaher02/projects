import random
import string


filewrite = input("Do you want to write on a file (y/n)? ")

if filewrite == "y": 
    passlocation =  input("Where are you using your password? ")
    username = input("What is the username? ")
    charlength = int(input("How long do you want your password? "))

    charset = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(charset) for i in range(charlength))

    f = open("password.txt", "a")
    f.write(" \n \n" + passlocation + ": \n")
    f.write("  username: " + username + "\n")
    f.write("  password: " + password)
    f.close()

    print("\n" + passlocation + ":")
    print("  username: " + username)
    print("  password: " + password)
else: 
    charlength = int(input("How long do you want your password? "))

    charset = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(charset) for i in range(charlength))

    print("password: " + password)

input()