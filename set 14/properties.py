# create a class called temperature
class temperature:
	def __init__(self, __celcius):
		self.__celcius=__celcius

	@property
	def celcius(self):
		return self.__celcius

	@celcius.setter
	def celcius_setter(self, celcius):
		self.__celcius=celcius
		Validation(celcius)

	def Validation(self, x):
		if x < -270:
			print("Good: Temperature under control!")
		else:
			print("Warning: Temperature exceeding limit!")


temp_obj=temperature(-400)

temp_obj.celcius_setter()
