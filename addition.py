#program to keep adding a stream of numbers 
sum=0
while(True):
	userinput=input("enter the item price or press q to exit ")
	if(userinput!='q'):
		sum=sum + int(userinput)
		print(f"Order total so far :{sum}")
	else:
		print(f"Your bill total is {sum} . Thanks for shopping with us ")
		break
	
   #receipt
   
print("Prices of your items are :")
   