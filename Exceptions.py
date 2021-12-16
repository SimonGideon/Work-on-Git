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

