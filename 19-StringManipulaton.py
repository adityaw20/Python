# string in python are sequence of hcra enclosed in single or double quotes 
text = "Hello Python!"

# 1. Accesing char 
print(text[0]) # first char 
print(text[-1])# last char 

# 2.  String Slicing 
print(text[0:5]) # char from index 0 to 4
print(text[:5]) # from start to index 4 
print(text[7:]) # from index 7 to end 
print(text[::2]) # Every second char 
print(text[::-1]) # Reverse string 

#3 String Concatenation and repition
greeting = "Hello"
name = "abc"
print(greeting+" "+name)  #concatnation
print(greeting * 3) # Repitation

#4. Useful String Methods
sample = " Python Programming"
print(sample.lower()) # convert to lower case 
print(sample.upper()) # CONVERT to uppercase  
print(sample.strip()) # Remove Leading and trailing spaces
print(sample.replace("Python","java")) # Replace Text
print(sample.split()) # Split into list (By spaces) 
print("-".join(["Python" , "is", "sun"])) # join list with seperator

# 5 checking string content
word ="Python123"
print(word.isalpha())  # False -> contains numbers 
print("Python".isalpha()) # True -> only letters 
print(word.isdigit()) #False ->contains letters
print("12345".isdigit()) # True ->only Numbers
print(word.isalnum())# True -> Leters + numbers

# 6 Escape  Sequences 
print("Hello\nworld") #new line
print("Hello\tworld") # Tab space 
print("He said \"Python is awesome!\"") #double quote inside string 

# Assignmnet 
# Write a code for creating a simple calculator 
# take user input 2 numbers 
# then take input operator (- + / * // %)
# and give the output
