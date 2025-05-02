# create a class called Engine
class Engine:
	def __init__(self, fuel_type):
		self.fuel_type=fuel_type


class Car:
	engine_obj=Engine("Kerosene")

	def start_engine(self):
		print(f"{self.engine_obj.fuel_type}")

car=Car()

car.start_engine()