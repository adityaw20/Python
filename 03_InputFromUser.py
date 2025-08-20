# The input() function lets the user type somthng into the console 
# it lways return the input as a string 

# getting a string from user 
name = input("Enter Your NAme:-")
print("Hello ",name)

# geting an integer from user
# need to convert string to nt using int()
age =int(input("Enter your age:"))
print("You are",age,"Years old")

# getting a float fromuser 
height = float(input("Enter your height in meters:"))
print("Your Height is",height,"m")

# performing calculation fro user input
num1 = float(input("Enter 1st number:-"))
num2 = float(input("Enter 2nd number:-"))
sum_result  = num1 + num2
print("The sum is: ",sum_result) 

#combining inputs in a sentence
city = input("Enter your city:-")
print(f"{name} from {city} is {age} years old and {height}m Tall")

#NOTE:
# Always convert input to thee required type (int , float etc.)
# Or else calculation will not work as expected 