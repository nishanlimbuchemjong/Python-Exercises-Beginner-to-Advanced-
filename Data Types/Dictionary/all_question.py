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

# Q.3) Count the frequency of each character in a string using a dictionary.
print("Question-3:\n")

sentences = "My name is Nishan Limbu. I am studying BCA in Araniko Multiple Campus"
list_sentences = list(sentences)

freq = [list_sentences.count(i) for i in list_sentences]
character_dict = dict(zip(list_sentences, freq))

print(f"The sentence is {sentences}")
print(f"\nRequired Dicitonary after counting the frequenct of each character in a string: \n{character_dict}")
print("...............................................................\n")