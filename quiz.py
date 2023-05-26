print("Welcome to my computer quiz")
playing = input("Do you want to playing?   ")
if playing!="yes" :
    quit()
else:    
    print("Okay! lets play ")
score=0
answer =input("What does cpu stands for? ").lower()
if answer=="central processing unit" :
     print("COrrect!")
     score+=1
else:
    print("Incorrect") 
print("You got "  + str(score)+" questions correct")   