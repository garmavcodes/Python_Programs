# Python String Methods – Demo and Explanation

This script demonstrates various Python string methods with a sample string.

a = "!!!!heLLo My n!!ame is SHarika!!!!!!"  # The sample string

print(a.upper())           # Converts all letters to uppercase
print(a.lower())           # Converts all letters to lowercase
print(a.rstrip("!"))       # Removes trailing '!' characters
print(a.lstrip("!"))       # Removes leading '!' characters
print(a.strip("!"))        # Removes '!' from both ends
print(a.replace("SHarika", "ANjana"))  # Replaces 'SHarika' with 'ANjana'
print(a.split("a"))        # Splits the string at each 'a' into a list
print(a.capitalize())      # Capitalizes first letter, makes rest lowercase
print(len(a))              # Returns the length of the string (should be 36)
print(a.center(57, "*"))   # Centers the string within 57 chars, fills with '*'
print(a.count("!"))        # Counts the number of '!' characters
print(a.endswith("!"))     # Checks if string ends with '!'
print(a.endswith("!!", 5, 16)) # Checks if substring (index 5–15) ends with '!!'
print(a.find("My"))        # Finds index of 'My', returns -1 if not found
print(a.index("My"))       # Same as find(), but raises error if not found
print(a.isalnum())         # Checks if string is alphanumeric (letters + numbers)
print(a.isalpha())         # Checks if string has only alphabetic characters
print(a.islower())         # Checks if all letters are lowercase
print(a.isupper())         # Checks if all letters are uppercase
print(a.isprintable())     # Checks if all characters are printable
print(a.isspace())         # Checks if string has only whitespace
print(a.istitle())         # Checks if each word starts with an uppercase letter
print(a.startswith("!!"))  # Checks if string starts with '!!'
print(a.swapcase())        # Swaps case of each character (upper ↔ lower)
print(a.title())           # Capitalizes first letter of every word
print(a.zfill(50))         # Pads string with leading zeroes to length 50
