# SET (UNordered , mutable , no duplicates)

unique_num = {1,2,3,4,4}
print(unique_num) # duplicate removed auto

unique_num.add(5)
print(unique_num)
unique_num.discard(2)
print(unique_num)

# Set Operations 
a = {1,2,3,}
b = {3,4,5,}
print("Union:",a | b)
print("Intersection:",a & b)
print("Diffresnce:",a - b)
print("Symetric Diffresnce:",a ^ b)
