class Animal:
	def __init__(self, name):
		self.name=name

	def speak(self):
		pass

class dog(Animal):
	def speak(self):
		print("Bark!")

class cat(Animal):
	def speak(self):
		print("Meow!")

dog_obj= dog("Moleman")
cat_obj= cat("Felix")

def animal_sound(animal_obj):
	animal_obj.speak()

animal_sound(dog_obj)
animal_sound(cat_obj)