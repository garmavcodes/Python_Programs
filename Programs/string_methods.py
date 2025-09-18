a="!!!!heLLo My n!!ame is SHarika!!!!!!"
print(a.upper()) #makes upper
print(a.lower()) #makes lower
print(a.rstrip("!")) #makes right strip
print(a.lstrip("!")) #makes left strip
print(a.strip("!")) #makesboth side strip
print(a.replace("SHarika","ANjana")) #replace word
print(a.split("a")) #makes a list and split by a
print(a.capitalize()) #makes first letter capital and rest small
print(len(a)) #the length of string is 36
print(a.center(57,"*")) #makes the string in center with len 57 and fill spaces with * and if the len is less then just same string
print(a.count("!")) #counts to no of ! in string
print(a.endswith("!")) #ckecks if string end with ! and return true/false
print(a.endswith("!!",5,16)) #checks if string end with !! in the given range
print(a.find("My")) #finds index of My and if not gives-1
print(a.index("My")) #finds index of My and if not gives error
print(a.isalnum()) #checks if string has only alphabets and numbers
print(a.isalpha()) #only alphabets
print(a.islower()) #checks if string is lower
print(a.isupper())#checks if string is upper
print(a.isprintable()) #checks if string is printable and non printables are \n \t etc
print(a.isspace()) #checks if string has only spaces
print(a.istitle()) #checks if all the first letter of word is caplital
print(a.startswith("!!")) #checks if string start with!!
print(a.swapcase())#swaps the cases
print(a.title())#makes all first letter of each word capital
print(a.zfill(50))#fills the string with 0 only from left to make len 50
