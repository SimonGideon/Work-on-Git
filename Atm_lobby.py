#Atm lobby auth process for pin for the card.
print("Enter your Atm Card to proceed")
class login(object):
	"""log in abstract  fro ATM lobby"""
	def __init__(self, pin):
		self.pin = pin
		self.error = "Enter a valid pin"
	def check(self):
		try:
			if (self.pin == pin):
				print("Log in successfull Proceed to dashboard")
                #user directed to the dashboard to allow withdrawal and checking
                #balance
			else:
				print(self.error)
			finally:
				pass
login = login("1097")
pin = int(input("Enter pin"))
log.check()

		
