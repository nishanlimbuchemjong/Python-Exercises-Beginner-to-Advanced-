# Q.1) Write a function that takes a string and returns the number of characters in it

def number_of_characters(sentence):
    total_character = len(sentence)
    return total_character

sentences = input("Enter any string (word or sentences): ")

result = number_of_characters(sentences)
print(f"Total characters in '{sentences}'\n{result}")
print("..............................................\n")

# Q.2) Create a function that takes a list of numbers and returns a new list with each number squared

def squared_number(numbers):
    return [x**2 for x in numbers]

list_num = [1, 2, 3, 4, 5]
result = squared_number(list_num)
print(f"Squared of a number list {list_num} = {result}")
print("..............................................\n")

# Q.3) Write a function that checks if a given number is prime

def is_prime(num):
    if num > 0:
        if num % 2 == 0 or num % 3 == 0:
            if num == 2 or num == 3:
                return True
            return False
        else:
            return True
    else:
        return False

num = 2
result = is_prime(num)

if result == True:
    print(f"{num} is prime number")
else:
    print(f"{num} is not a prime number")
    
print("..............................................\n")

# Q.4) Define a function that takes a list and returns the largest element in the list.
def largest_element(numbers):
    largest = max(numbers)
    return largest

list_num = [109, 22, 34, 42, 55]
result = largest_element(list_num)
print(f"Largest element of a  list {list_num} = {result}")
print("..............................................\n")


# Q.5) Implement a function that calculates the sum of all even numbers in a given range.

def sum_of_even(size):
    sum = 0
    for i in range(1, size+1):
        if i % 2 == 0:
            sum += i
    return sum

num = 10
result = sum_of_even(num)
print(f"Sum of even number upto {num} = {result}")
print("..............................................\n")

# Q.6) Write a function that takes a dictionary and returns a list of its keys.
def list_of_keys(dictionary):
    return [x for x in dictionary.keys()]

personal_info = {
    "Name": "Nishan Limbu",
    "Grade": "BCA 7th sem"
}

result = list_of_keys(personal_info)
print(f"List of all keys in dictionary {personal_info} is given below:\n{result}")
print("..............................................\n")

# Q.7) Create a function that takes a string and returns the string with all vowels removed.

def vowels_removal(sentence):
    vowels_letters = ['a', 'e', 'i', 'o', 'u']
    sentence_list = list(sentence)
    for i in sentence_list:
        if i == 'a' or i == 'e' or i =='i' or i == 'o' or i == 'u':
            sentence_list.remove(i)

    return sentence_list

sentences = "Nishan Limbu"
result = vowels_removal(sentences)
print(f"After removing vowels from {sentences}, we get\n\t")
for i in result:
    print(i, end=(""))

print("\n..............................................\n")


# Q.8) Write a function that takes a list of strings and returns the longest string in the list.
def longest_string(sentences_list):
    char_count_list = []
    for i in sentences_list:
        char_count_list.append(len(i))

    max_index = char_count_list.index(max(char_count_list))
    return sentences_list[max_index]

sentences_list = ['Nishan Limbu', 'Numa Limbu', 'Anu Limbu', 'Dipa Limbu']

result = longest_string(sentences_list)
print(f"Lonest string in a given list {sentences_list} is {result}")
print("................................................................\n")


# Q.9) Implement a function that takes a string and counts how many times each character appears in it

def counting_characters(sentences):
    sentence_dict = {}
    for i in sentences:
        sentence_dict[i] = sentence_dict.get(i, 0) + 1
    return sentence_dict

sentences = "NishanddddssNN"
result = counting_characters(sentences)
print(result)
print("................................................................\n")

# Q.10) Write a function that accepts a list and returns a new list with duplicate elements removed
print("Question-10:")
def duplicate_remove(given_list):
    new_list = []

    for i in given_list:
        if i not in new_list:
            new_list.append(i)
    return new_list
        
user_list = [1, 5, 6, 5, 5, 5, 1, 2, 3, 6, 7, 7]
result = duplicate_remove(user_list)
print(result)
print("................................................................\n")

