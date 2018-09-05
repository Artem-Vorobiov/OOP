print('\n')

class Employee:

	raise_amount = 1.04		# CLASS VARIABLES
	num_of_ems   = 0 		# CLASS VARIABLES

	def __init__(self, first, last, pay):
		self.first = first								# Instantce
		self.last = last								# Instantce
		self.email = first + '.' + last + '@email.com'	# Instantce
		self.pay = pay									# Instantce

		Employee.num_of_ems += 1

	def fullname(self):
		return '{} {}'.format(self.first, self.last)

	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amount)

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)
 
print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)
print('\n')


print(emp_1.__dict__)
print(Employee.__dict__)
print('\n')

emp_1.raise_amount = 1.9

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)
print('\n')

print(Employee.num_of_ems)