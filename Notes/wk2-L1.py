# Week 2 Lesson 1

# Intro to Programming
# Strings

# Make sure to use F strings for all print statements
# EXAMPLE

name = "John"
last_name = "Doe"

print(f"Hello {name} {last_name}") # Using f strings
# Output: Hello John Doe

print("Hello " + name + " " + last_name) # Using concatenation
# Output: Hello John Doe

print("Hello {} {}".format(name, last_name)) # Using format
# Output: Hello John Doe

# As you can see f strings are the easiest to use and read


# When printing a variable in a string you need to convert it to a string
# EXAMPLE

username_input = input("Enter your username: ")
temp_cel = input(f"Hi {username_input}, enter the temperature in Celcius: ")
temp_cel = int(temp_cel) # Convert the string to an integer

temp_fah = int((temp_cel * 9/5) + 32) # Convert Celcius to Fahrenheit

print("The temperature in Fahrenheit is: " + str(temp_fah)) # Convert the integer to a string

# However using f strings will automatically convert the variable to a string e.g
print(f"The temperature in Fahrenheit is: {temp_fah}")


# String Methods


# capitalize()
# This method capitalizes the first letter of the string
cap_me = "capitalize me"
print(cap_me.capitalize()) # Returns "Capitalize me"
print(cap_me) # Returns "capitalize me"


# title()
# This method capitalizes the first letter of each word in the string, also known as title case
title_me = "title me"
print(title_me.title()) # Returns "Title Me"
print(title_me) # Returns "title me"


# lower()
# This method makes all letters in the string lowercase
lower_me = "LOWER ME"
print(lower_me.lower()) # Returns "lower me"
print(lower_me) # Returns "LOWER ME"


# upper()
# This method capitalizes all letters in the string
upper_me = "upper me"
print(upper_me.upper()) # Returns "UPPER ME"
print(upper_me) # Returns "upper me"


# replace()
# This method replaces a string with another string
replace_me = "replace me"
print(replace_me.replace("me", "you")) # Returns "replace you"
print(replace_me) # Returns "replace me"

# join()
# This method joins a list of strings together
join_me = ["join", "me"]
print(" ".join(join_me)) # Returns "join me"
print(join_me) # Returns ["join", "me"]

# count()
# This method counts the number of times a string appears in another string
count_me = "count me and me and me!"
print(count_me.count("me")) # Returns 3
print(count_me) # Returns "count me and me and me!"


# Combining replace() and title()
# EXAMPLE

message = "This is a string with a lot                  of spaces"

print(f'Original message: {message}')

titled_message = message.title()
print(f'Titled message: {titled_message}')

replaced_message = titled_message.replace(" ", "")
print(f'Replaced message: {replaced_message}')

# Output
# Original message: This is a string with a lot                  of spaces
# Titled message: This Is A String With A Lot                  Of Spaces
# Replaced message: ThisIsAStringWithALotOfSpaces


# Removing spaces with strip(), lstrip(), and rstrip()

# strip() EXAMPLE
strip_me = "     strip me     "
print(strip_me.strip()) # Returns "strip me"

# lstrip() EXAMPLE
lstrip_me = "     lstrip me     "
print(lstrip_me.lstrip()) # Returns "lstrip me     "

# rstrip() EXAMPLE
rstrip_me = "     rstrip me     "
print(rstrip_me.rstrip()) # Returns "     rstrip me"