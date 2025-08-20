# variable are containers to store data values.
#In python, you don't need to declaree the type explicitlty

#assigning integer value to variable
#int age=123;
age=123 # integer type

# Assigning floating point value 
# float height =123.123f;
height=123.123 # float type

# Assigning string value 
# char ch[] = "abcd";
name = "abcd" #tring type 

# assigning boolen value 
is_student = True # boolean type (True/False)

#python can store multiple values in one variable using data structure
fruits =["Apple","Banana","Cherry"] #List
coordinates =(10,20)  #Tuple  (Immutable list)
unique_numbers ={1,2,3,4,5}  # set (NO duplicates)
person = {"name":"abcd","age":"123"} # dictinory (key-value pairs)

# printing variables
print("Name:",name)
print("Age:",age)
print("Height:",height)
print("Is Student",is_student)

# checking type of variables 
print("type of 'age':",type(age))
print("type of 'fruits':",type(fruits))
print("type of 'person':",type(person))

# Dynamic typing : you can reassign variable to diffrent type
x=10
print(x,type(x)) #int 
x = "Now i'm a string"
print(x,type(x)) #str