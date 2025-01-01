# Q.1) Find the common elements between two sets.
print("Question-1:\n")
number_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "Numbers"}
mixed_set = {"Nishan", "Limbu", 5, 10, 2, "Numbers","Chemjong", "AI Engineer"}

common_set = number_set & mixed_set

print(f"Number set: {number_set}")
print(f"Mixed set: {mixed_set}")
print(f"\nCommon set between Number and Mixed set = {common_set}")
print("................................................................/n")

# Q.2) Write a program to remove all duplicates from a list using a set.
print("Question-2: \n")
number_list = [33, 43, 56, 33, 22, 43, 30, 22, 45, 75, 75]
number_set = set(number_list)

print(f"Before converting the list into set, \nList = {number_list}")
print(f"After removing all duplicates from a list, we get\n\t{number_set}")
print(".............................................................\n")