'''
snake 1, water-1, gun 0
1 & -1 = 1
1 & 0 = 0
-1 & 0 = -1

'''
import random
computer=random.choice([1, -1, 0])
actual_dict={"s":1,"w":-1,"g":0}
rev_dict={1:"s",-1:"w",0:"g"}
choice=input("Enter your choice (s,w,g):")
you=actual_dict[choice]
print("****RESULT****")
print(f"computer choice:{rev_dict[computer]}\nyour choice:{choice}")
if(you==computer):
    print("It's Draw..")
else:
    if(you==1 and computer==-1):
        print("You won!!!!")
    elif(you==1 and computer==0):
        print("you loss")
    elif(you==-1 and computer==1):
        print("you loss")
    elif(you==-1 and computer==0):
        print("You won")
    elif(you==0 and computer==-1):
        print("you loss")
    elif(you==0 and computer==1):
        print("you won")
    else:
        print("Something went wrong.. ")
