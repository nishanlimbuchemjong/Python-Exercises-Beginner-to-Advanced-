# Enumerate a List
# Use the enumerate() function to iterate through the list ['apple', 'banana', 'cherry'] with an index.

fruits = ['apple', 'banana', 'cherry']

enumerate_result = enumerate(fruits)

# printing the enumberator objects 
for i, j in enumerate_result:
    if i == 2:
        print(j)

