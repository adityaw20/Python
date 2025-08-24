# Lists (Ordered, Mutable , Allows Duplicates)

fruits = [ "Apple", "Banana" ,"Cherry"]
print(fruits)

# Accessing Elements 1 by 1
print(fruits[0]) # first element
print(fruits[1]) # second element
print(fruits[-1]) # last  element

# Modify list 
fruits[1] = "Mango"
print(fruits)

# Adding Elements 
fruits.append("orange") # Add at end
print(fruits)
fruits.insert(1 , "Kiwi") # add at specific index
print(fruits)

# Removing elements
fruits.remove("Apple") # Removeby value 
print(fruits)
popped_item = fruits.pop() # Remove last item 
print(fruits)
print("Popped:",popped_item)
del fruits[0] # Remove by index
print(fruits)

# list slicing 
numbers = [1,2,3,4,5 ]
print(numbers[1:4]) # Element from index 1 to 3
print(numbers[:3]) # first 3 elements
print(numbers[::2])  # Every 2nd element
