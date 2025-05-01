# creating class dog
class car:
	def __init__(self, brand, type):
		self.brand=brand
		self.type=type

	def rev(self):
		print("Vroom! Vroom!")

class driver:
	def __init__(self, deals, region):
		self.deals=deals
		self.region=region

	def driver_and_car(self, driver_name, car_obj):
		print(f"The Driver's name is {driver_name}, and the car he drives is a {car_obj.type}")


car_object=car("Toyta", "racecar")
driver_object=driver("Romanian Deal", "Romanian")

driver_object.driver_and_car("Tommy", car_object)