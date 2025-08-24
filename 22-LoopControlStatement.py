# Loop Control Statement 
# break ->Exit loop Immediately 

for i in range(10):
    if i == 5:
        break 
    print(i)

# continue -> Skip current iteration 
for i in range(5):
    if i == 2:
        continue
    print(i)

# Else wwith loops -> runs when loop completes without break  
for i in range(3):
    print(i)
else :
    print("Loop Completed!") # Runs becouse no break happened