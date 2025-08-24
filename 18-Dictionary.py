# DICTIONARY (Key- value pairs , unordered)

person = {"name":"Aditya","age":"22","city":"pune"}
print(person)

#access values 
print(person["name"]) # Using key 
print(person.get("age"))  # safer method

# ADD/ Updates
person["age"] = 25
print(person)
person["country"] = "India"
print(person)

# LOOps through distionary 
for key , value in person.items():
    print(key ,":",value)
