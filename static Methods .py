# item1 = 'Phone'
# item1_price = 100
# item1_quantity =5
# item1_price_total = item1_price*item1_quantity
# print(item1_price_total)
import csv
class Item():
	pay_rate = 0.8 #The pay rate after 20% Discount
	all = []
	def __init__(self, name: str, price: float, quantity=0):
		# 0 is passed in when the quantity is not known
		#Run  validation to receive arguents
		assert price>=0, f"Price {price} is not greater thanzero"
		assert quantity>=0, f"Price {quantity} is not greater thanzero"
		#assing to self object

		self.name = name
		self.price = price
		self.quantity = quantity

		# Ations to execute
		Item.all.append(self)

	def calculate_total_price(self):
		return self.price*self.quantity
	def apply_discount(self):
		self.price = self.price * self.pay_rate
	@classmethod
	def instantiate_from_csv(cls):
		with open('items.csv', 'r') as f:
			reader = csv.DictReader(f)
			items = list(reader)
		for item in items:
			Item(
				name=item.get('name'),
				price=float(item.get('price')),
				quantity=int(item.get('quantity'))
				)
	@staticmethod
	def is_integer(num):
		if isinstance(num, float):
			#counting out the floats that are point zero
			return num.is_integer()
		elif isinstance(num, int):
			return True

	def __repr__(self):
		return f"Item('{self.name}', {self.price}, {self.quantity})"
print(Item.is_integer(7.5))