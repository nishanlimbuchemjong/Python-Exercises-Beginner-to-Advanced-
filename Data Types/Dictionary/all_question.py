# Q.1) Create a dictionary where keys are numbers from 1 to 5, and values are their squares.
print("Question-1:\n")
dict_numbers = {x:x**2 for x in range(1, 6)}

print(f"Dictionary created where keys are numbers from 1 to 5, and values are their squares:\n\t{dict_numbers}")
print(".................................................................\n")

# Q.2) Write a program to merge two dictionaries.
print("Question-2:\n")

number_dict = {"Name":"Nishan", "Grade": "BCA 7th Sem"}
fav_sub_dict = {"Books": ["Science", "Mathematics", "Optional Math"]}

number_dict.update(fav_sub_dict)

print(f"Number Dictionary = {number_dict}\nFavourite Subject Dictionary = {fav_sub_dict}")
print(f"\nAfter merging two dictionaries, we get \n\t{number_dict}")
print("...............................................................\n")