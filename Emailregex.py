import re 
email_validation="^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
user_email=input("Enter your email:  ")

if re.search(email_validation,user_email):
     print("Vlaid Email")
else :
     print("Invalid Email")     