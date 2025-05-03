# create a class called counter
class counter:

	# create class variable named count
	count=0

	def __init__(self):
		pass

	@classmethod
	def increment_count(cls):
		cls.count+=1
		return cls.count

count_obj=counter()

print(f"{counter.increment_count()}")
print(f"{counter.increment_count()}")
print(f"{counter.increment_count()}")
print(f"{counter.increment_count()}")
print(f"{counter.increment_count()}")