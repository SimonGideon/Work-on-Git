print("ENTER THE FOLLOWING DETAILS TO SIGN UP")
name = input("Enter your full name\n")
username = input("Enter your user name\n")
password = input("Enter password\n")
password_confirmation = input("Re-enter your password\n")


def account_creation():
    if password == password_confirmation:
        print("Account created successfully")
    else:
        print("Wrong credentials entered")


account_creation()

print("Proceed to log in to your account")
UserName = input("Enter your username\n")
Password = input("Enter your password\n")


def log_in():
    if password == Password and UserName == username:
        print("Logged in successfully")
    else:
        print("Wrong details entered.Username does not match password")


log_in()