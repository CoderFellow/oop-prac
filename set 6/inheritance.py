class Animal:
	def __init__(self, name):
		self.name=name

	def speak(self, generic_animal_sound):
		print(f"{generic_animal_sound}!")

class dog(Animal):
	def speak(self):
		print("Bark!")

class cat(Animal):
	def speak(self):
		print("Meow!")

dog_obj= dog("Moleman")
cat_obj= cat("Felix")

dog_obj.speak()
cat_obj.speak()