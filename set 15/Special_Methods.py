# create class called point
class Point:
	# x and y points
	def __init__(self, x, y):
		self.x=x
		self.y=y

	# implementing the special method str
	def __str__(self):
		return f"({self.x},{self.y})"

	# implementing the special method add
	def __add__(self, other):
		if isinstance(other, Point):
			new_x=self.x+self.x
			new_y=self.y+self.y
			return Point(new_x, new_y)
		else:
			return NotImplemented

# create point objects
first_point=Point(1, 2)
second_point=Point(3, 4)

# Using __str__ implicitly with the string function
print(first_point)
print(second_point)

# using the add with the + operator
sum_of_two_points=first_point+second_point
print(sum_of_two_points)

# Trying to add a point to something that's not a point
result=first_point+5
print(result)