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

# Q.3) Check if a set is a subset of another set.
print("Question-3: \n")

domestic_animal_set = {"Dog", "Cow", "Donkey", "Horse", "Buffalo"}
animal_set = {"Lion", "Leopard", "Dog", "Giraffe", "Cow", "Tiger", "Donkey", "Horse", "Buffalo"}

result = domestic_animal_set.issubset(animal_set)

print(f"Sets:\nDomestic Set = {domestic_animal_set}\nAnimal Set = {animal_set}\nResult:")
if result == True:
    print("\tYes, Domestic set is the subset of Animal set")
else:
    print("\tNo, Domestic set is the subset of Animal set")
print("............................................................................\n")

# Q.4) Write a program to find the symmetric difference between two sets.
print("Question-4:\n")

domestic_animal_set = {"Dog", "Cow", "Donkey", "Horse", "Buffalo"}
animal_set = {"Lion", "Leopard", "Dog", "Giraffe", "Cow", "Tiger", "Donkey", "Horse", "Buffalo"}

result = domestic_animal_set.symmetric_difference(animal_set)

print(f"Sets:\nDomestic Set = {domestic_animal_set}\nAnimal Set = {animal_set}\nResult:")
print(f"Symmbertic Difference between two sets = {result}")
print(".................................................\n")