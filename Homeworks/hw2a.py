#login system
print("******login******")
userEmail = "elif"
userPassword = "trytrytry"

logEmail = input("Please enter your email:")
logPassword = input("Please enter your password:")

if (userEmail == logEmail):
    if (userPassword == logPassword):
        print("Logged in successfully")
    else:
        print("Wrong password")
elif (userEmail != logEmail and userPassword != logPassword):
    print("Wrong email and password")
else:
    print("Wrong email")
    
