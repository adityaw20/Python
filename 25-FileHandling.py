# FIle handling allows reading and writing data to files.
# MODES
# 'r' -> Read  (Fie must exist)
# 'w' -> Write (Create new file or overwrites existing)
# 'a' -> Append (Creates new file if not exits)
# 'rb'-> Read binary 
# 'wb'-> Write binary 

# 1. Writing to a file 
file = open("Example.txt","w")  # open in write mode
file.write("Hello, Python \n")  # Write Text
file.write("This is a file handling example.\n")
file.close() #always close the file

# 2. Reading from file 
file = open("Example.txt","r")  # open in read mode
content = file.read() # rRead entire file 
print("File Contect:\n",content)
file.close()

# 3. Reading line by line 
file = open("Example.txt","r")  # open in read mode
for line in file:
    print("Line:",line.strip()) # strips() remove new line
file.close()

# 4. Appending to a file 
file = open("Example.txt","a")  # open in append mode
file.write("This is was added later.\n")
file.close()

# 5. Using 'with' statement (auto-closes file)
with open("Example.txt","r") as file:
    print("First line:",file.readline()) # REad one line

with open("Example.txt","r") as file:
    lines = file.readlines() # return list of all
    print("All lines as list:",lines)

# 6. Writing & Reading Binari file
# Writing Binary
with open("binary_file.bin","wb") as file:
    file.write(b'\x48\x65\x6C\x6C\x6F') # 'Hello' in bytes

with open("binary_file.bin","rb") as file:
    data = file.read()
    print("Binary data:",data)