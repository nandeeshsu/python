import logging

print("hello world")

logger = logging.getLogger(__name__)

class Employee:
    
	def __init__(self, firstName, lastName):
		self.firstName = firstName
		self.lastName = lastName

	def __str__(self):
		return "Employee("+self.firstName + "," + self.lastName + ")"

	def getFirstName(self):
		return self.firstName

employee = Employee("Nandeesh", "subbegowda")
print(employee)
logger.warning(employee.getFirstName())

print(__name__)
print(Employee.__dict__)

