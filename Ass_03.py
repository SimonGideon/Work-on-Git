
def login():
	print("-----Log in! -----")
	_username = input("Username: ")

	_password = input("Password: ")
	if _username == username and _password == password:
		print("--Log In Successfuly-- Welcome:", username)

print("Helo Welcome to the log in System!!")
n = input("Do you have an account ?(Y/N): ")
if n.title()=="N":
	print("Sign Up with The following details --->")
	firstname = input("First Name: ")
	lastname = input("Last Name: ")
	username = input("Username: ")
	password = input("Password: ")
	confirm_password = input("Retype your password: ")
	while confirm_password != password:
		confirm_password = input("Retype your password: ")
	else:
		print("Hello", firstname, "account Created Successfuly")
		login()
else:
	login()
