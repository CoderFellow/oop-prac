# creating class car
class car:
	def __init__(self, brand, type):
		self.brand=brand
		self.type=type

# creating objects of the car class
my_car=car("Ford", "sportscar")
dads_car=car("Toyota", "truck")

# accessing the attributes of the object
print(f"My car's brand is {my_car.brand}, and it's type is that of a {my_car.type}")
print(f"My dad's car brand is {dads_car.brand}, and it's type is that of a {dads_car.type}")
