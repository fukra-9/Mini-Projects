class Atm:
	def __init__(self):
		self.__pin=''
		self.__balence=0
		self.menu()
	def get_pin(self):
		return self.__pin
		
	def set_pin(self,new_pin):
		if type(new_pin)==str:
			self.__pin= new_pin
			print("pin set sucessfull")
		else :
			print("not allowed")
	def menu(self):
		user_input = input('''
					Hello,how would you like to proceed ?
					1.Enter 1 to create pin 
					2.Enter 2 to deposit 
					3.Enter 3 to withdraw 
					4.Enter 4 to check balence 
					5.Enter 5 to exit
''')
		if user_input=='1':
			self.create_pin()
		elif user_input=='2':
			self.deposit()
		elif user_input=='3':
			self.withdraw()
		elif user_input=='4':
			self.check_balence()
		else :
			print("bye")
			
	def create_pin(self):
		self.__pin = input("Enter your pin")
		print("pin set successful")
		
	def deposit(self):
		temp=input("Enter your pin")
		if temp == self.__pin:
			amount =int(input("Enter the amount"))
			self.__balence = self.__balence + amount
			print("Amount entered sucessfull")
		else:
			print("invalid pin")
			
	def withdraw(self):
		temp=input("Enter your pin")
		if temp == self.__pin:
			amount =int(input("Enter the amount"))
			if amount<self.__balence:
				self.__balence=self.__balence-amount
				print("operation sucessfull")
			else :
				print ("insufficient balence")
		else :
			print("invalid pin")
			
	def check_balence(self):
			temp=input("Enter your pin")
			if temp == self.__pin:
				print(self.__balence)
			else :
				print("Invalid pin")	
			
		
Atm()			
		
		
		