import time #library for time functions
name=input("Enter your name:")
now=time.localtime() #current time
print("current time:",time.strftime("%I-%M-%S %p",now)) # prints time in 12-h format with AM/PM
h=int(now.tm_hour) #hour
if(h>=0 and h<12): 
  print("good morning,",name)
elif(h>=12 and h<16):
  print("good afternoon,",name)
elif(h>=16 and h<20):
  print("good evening,",name)
elif(h>=20 and h<24):
  print("good night,",name)
else:
  print("error") #this will never happen until something goes wrong
