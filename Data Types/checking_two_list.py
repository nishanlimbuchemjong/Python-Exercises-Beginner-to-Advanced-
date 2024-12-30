"""
Write a program to check if two lists contain any common elements.
"""
fav_sub_student1 = ['Math', 'Science', 'Economic', 'Health']
fav_sub_student2 = ['C programming', 'DSA', 'Math', 'Python']


common_element = [i for i in fav_sub_student1 if i in fav_sub_student2]

# printing the result:
print(f"List-1 = {fav_sub_student1}\nList-2 = {fav_sub_student2}")
print("\nCommon Element between two list:")
for i in common_element:
    print(i)

