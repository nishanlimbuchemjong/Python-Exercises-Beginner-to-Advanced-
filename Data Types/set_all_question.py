"""
All Question related to 'Set in Python'
"""

# Q.1) Convert the list [1, 2, 2, 3, 4, 4, 5] into a set to remove duplicates.
print("Quesiton-1: Convert List to Set\n")

# initializing the number list
numbers_list = [1, 2, 2, 3, 4, 4, 5]

# converting the given list into set
numbers_set = set((numbers_list))

# printing the result
print(f"After removing duplicates from list {numbers_list}, we get")
print(numbers_set)
print("``````````````````````````````````````````````````\n")

"""
Q.2) Write a program to find common elements in three sets:
set1 = {1, 2, 3}
set2 = {2, 3, 4}
set3 = {3, 4, 5}
"""
print("Question-2: Common Elements in Multiple Sets")

# initializing the multiple sets:
set1 = {1, 2, 3}
set2 = {2, 3, 4}
set3 = {3, 4, 5}

# finding out the common element from three sets
set4 = set1 & (set2 & set3)

# printing out the common elemnts
print("Given sets")
print(f"Set-1 : {set1}")
print(f"Set-2 : {set2}")
print(f"Set-3 : {set3}")
print(f"\nCommon elements among three given sets are: ")

if set4:
    for i in set4:
        print(i)
else:
    print("\nThere is no common elements")
print("```````````````````````````````````````````````\n")

# Q.3) Create a set comprehension to generate a set of squares for numbers from 1 to 10.
print("Question-3: Set Comprehension\n")

# set comprehension for generating set of squares between 1 to 10
square_set = {i**2 for i in range(1, 10+1)}

# printing the result
print(f"Required set = {square_set}")
print("`````````````````````````````````````````````````````````````\n")
