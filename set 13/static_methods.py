# define methods that belong to a class but don't belonog to instance or the class itself.
class calculator:
	def __init__(self):
		pass

	@staticmethod
	def add(num1, num2):
		return num1 + num2

result=calculator.add(1, 2)
print(result)