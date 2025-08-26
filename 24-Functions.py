# Functions are reusable blocks of the code that  perform a  specific task 
# They help in code reusability and organization

# 1. Define and calling funtion
def greet():
    """This function prints the greeting massage"""
    print("Hello!, Welcome to python")

# calling the function
greet()

# 2.Function with parameters 
def greet_person(name):
    """Greeta person with their  name."""
    print(f"Hello, {name}!")

greet_person("Abcd")

# 3. Function with multiple parametrs 
def add_numbers(a,b):
    """return the summ of two numbers."""
    return a + b  # return send value back to caller 

result = add_numbers(5,3)
print("Sum is:",result)

# 4. Function with defoult values 
def greet_city(name, city ="pune"):
    """Greet with name and defoult city"""
    print(f"{name} is from {city}.")

greet_city("abcd") #uses defoult city
greet_city("abcdef","Delhi")  # overrides defoult

# 5. Function with keyword arguments
def student_info(name,age):
    print(f"Name:{name},Age:{age}")

student_info(age=123,name="acd") # order doesant matters with keywords
