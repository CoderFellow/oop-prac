from abc import ABC, abstractmethod
from math import*


# Create an abstract base class called Shape using the abc module
class Shape(ABC):
	@abstractmethod
	def area(self):
		pass

	@abstractmethod
	def perimeter(self):
		pass

class Rectangle(Shape):
	def __init__(self, length, width):
		self.length=length
		self.width=width

	def area(self):
		return self.length * self.width

	def perimeter(self):
		return 2 * self.length + 2 * self.width

class Circle(Shape):
	def __init__(self, radius):
		self.radius=radius

	def area(self):
		return math.pi * self.radius**2

	def perimeter(self):
		return 2 * math.pi*self.radius

rect_obj=Rectangle(2, 3)
print(f"Area of rectangle: {rect_obj.area()}")