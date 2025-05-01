# creating class dog
class car:
	def __init__(self, brand, type):
		self.brand=brand
		self.type=type

	def rev(self):
		print("Vroom! Vroom!")

car_object=car("a", "b")
car_object_II=car("","")

car_object.rev()
car_object_II.rev()