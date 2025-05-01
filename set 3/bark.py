# creating class dog
class car:
	def __init__(self, brand, type):
		self.brand=brand
		self.type=type

	def bark(self):
		print("Vroom! Vroom!")

car_object=car("a", "b")

car_object.bark()