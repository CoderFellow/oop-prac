# create a class called BankAccount
class BankAccount:
	def __init__(self, account_holder, __balance):
		self.account_holder=account_holder
		self.__balance=__balance

	# getter method for balance
	def get_balance(self):
		return self.__balance

	# setter method for balance
	def set_balance(self, new_balance):
		self.__balance=new_balance

	# deposit method
	def deposit(self, deposited_amount):
		current_balance=self.get_balance()
		new_balance = current_balance + deposited_amount
		self.set_balance(new_balance)
		print(f"New balance after deposit: {self.get_balance()}")

bank_acc_object=BankAccount("Mr. Donald", 2000)

try:
	print(bank_acc_object.__balance)
except AttributeError as e:
	print(f"Error accessing __balance directly: {e}")

bank_acc_object.deposit(200)