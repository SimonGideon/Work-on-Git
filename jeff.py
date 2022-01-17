import sqlite3
conn = sqlite3.connect('Users details.db')
c = conn.cursor()
# # creating table
# c.execute('''CREATE TABLE user_data
#   (Name text, Username text, Password VarChar)''')
# print("ENTER THE FOLLOWING DETAILS TO SIGN UP")
name = input("Enter your full name\n")
username = input("Enter your user name\n")
password = input("Enter password\n")
password_confirmation = input("Re-enter your password\n")


c.execute("INSERT INTO user_data VALUES ('name', 'username', 'password')")
#save and commit the changes
conn.commit()
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
    if password == Password and UserName == Username:
        print("Logged in successfully Welcome:", UserName )
    else:
        print("Wrong details entered.Username does not match password")


log_in()