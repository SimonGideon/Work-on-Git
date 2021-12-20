class EvenOnly(list):
	"""docstring for EvenOnly"""
	def append(self, integer):
		if not isinstance(integer, int):
			raise TypeError("Only integer can be added")
		if integer % 2:
			raise ValueError("Only even numbers can be added")
		super().append(integer)
e = EvenOnly()
e.append(2)

# Effects of exceptions
def no_return():
	print("Raising an exception")
	raise Exception("This will be raised")
	print("This will not be executed")
	return "I wont be run"

#Auth
import hashlib
class User:
	def __init__(self, username, password):
		"""Create a new user object. The password will be encrypted before storing"""
		self.username = username
		self.password = self.encrypt_pw(password)
		self.is_logged_in = False
	def __encrypt_pw(self, password):
		"""Encrypt the password with the username and return the sha digit"""
		hash_string = self.username+password
		hash_string = hash_string.encode("utf8")
		return hashlib.sha256(hash_string).hexadiget()
	def check_password(self, password):
		"""Returns true if the password is valid and false when invalid, otherwise"""
		encrypted = self.__encrypt_pw(password)
		return encrypted == self.password

class AuthException(Exception):
	def __init__(self, username, user=None):
		super().__init__(username, user)
		self.userame = username
		self.user = user
class UsernameAlreadyExists(AuthException):
	pass
class PasswordTooshort(AuthException):
	pass
 def login(self, username, password):
 	try:
 		user = self.users[username]
 	except KeyError:
 		raise InvalidUsername(username)
 	if not user.check_password(password):
 		raise InvalidPassword(username, user)
 	user.is_logged_in = True
 	return True
 def is_logged_in(self, username):
 	if username in self.users[username].is_logged_in
 return False
authenticator = Authenticator()