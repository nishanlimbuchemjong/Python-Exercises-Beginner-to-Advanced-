# Q.1) Write a function that takes a string and returns the number of characters in it
print("Question-1:\n")
def number_of_characters(sentence):
    total_character = len(sentence)
    return total_character

sentences = input("Enter any string (word or sentences): ")

result = number_of_characters(sentences)
print(f"Total characters in '{sentences}'\n{result}")
print("..............................................\n")

# Q.2) Create a function that takes a list of numbers and returns a new list with each number squared
print("Question-2:\n")
def squared_number(numbers):
    return [x**2 for x in numbers]

list_num = [1, 2, 3, 4, 5]
result = squared_number(list_num)
print(f"Squared of a number list {list_num} = {result}")
print("..............................................\n")

# Q.3) Write a function that checks if a given number is prime
print("Question-3:\n")
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
print("Question-4:\n")
def largest_element(numbers):
    largest = max(numbers)
    return largest

list_num = [109, 22, 34, 42, 55]
result = largest_element(list_num)
print(f"Largest element of a  list {list_num} = {result}")
print("..............................................\n")


# Q.5) Implement a function that calculates the sum of all even numbers in a given range.
print("Question-5:\n")
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
print("Question-6:\n")
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
print("Question-7:\n")
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
print("Question-8:\n")
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
print("Question-9:\n")
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
print("Question-10:\n")
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


# Q.11) Create a function that takes a list of numbers and returns their average
print("Question-11:\n")

def list_average(number_list):
    sum = 0
    for i in number_list:
        sum += i
    
    return sum / len(number_list)

number_list = [1, 2, 3, 4]
result = list_average(number_list)
print(f"Average of teh list of numbers {number_list} is {result}")
print("................................................................\n")

# Q.12) Write a function that accepts a string and a character and counts how many times the character appears in the string.
print("Question-12: \n")

def count_character(sentence, ch):
    total_count = 0
    for i in sentence:
        if i == ch in sentence:
            total_count += 1
    return total_count

words = "Nishan Limbu"
character = "i"

result = count_character(words, character)

print(f"'{character}' appears {result} times in {words}")
print("................................................................\n")


# Q.13) Define a function that reverses a list without using built-in reverse methods.
print("Question-13:\n")

def reverse_list(number_list):
    return number_list[::-1]

number = [1, 454, 2, 4, 7, 12]
result = reverse_list(number)

print(result)
print("................................................................\n")

# Q.14) Write a function that takes two lists and returns their intersection.
print("Question-14: \n")

def common_list(num_list1, num_list2):
    
    return list(set(num_list1).intersection(num_list2))

num1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
num2 = [2, 4, 6, 8, 10]

result = common_list(num1, num2)
print(f"Common elements in two list list1 = {num1} and list2 = {num2}\n= {result}")
print("................................................................\n")


# Q.15) Implement a function that takes a string and returns the number of words in it.
print("Question-15: \n")

def words_number(sentences):
    sent_list = list(sentences.split(' '))

    return len(sent_list)

sentence = "My name is Nishan Limbu"
result = words_number(sentence)
print(f"Total words in '{sentence}' is {result}")
print("................................................................\n")

# Q.16) Create a function that accepts a list of tuples and sorts them based on the second element of each tuple
print("Question-16: \n")

def sorted_list(lst):
    return sorted(lst, key=lambda x: x[1])
lst = [(11, 2454, 3, 4, 5), (6, 73, 8, 9, 10), (11, 123, 13, 14, 15)]
result = sorted_list(lst)
print(result)
print("................................................................\n")


# Q.17) Write a function that calculates the greatest common divisor (GCD) of two numbers.
print('Question-17: \n')

def greatest_common_divisor(num1, num2):
    factors = []
    if num1> num2:
        size = num1
    else:
        size = num2
    for i in range(1, size+1):
        if num1 % i == 0 and num2 % i == 0:
            factors.append(i)
    gcd = max(factors)
    return gcd

num1 = 10
num2 = 20
result = greatest_common_divisor(num1, num2)
print(f"The GDC of {num1} and {num2} is {result}")
print("................................................................\n")

# Q.18) Implement a function that generates all permutations of a given string.


# Q.19) Define a function that converts a given temperature from Celsius to Fahrenheit
print("Question-19: \n")

def celsius_to_fahrenheit(degree):
    return degree * (9 / 5) + 32

user_degree = 100

result = celsius_to_fahrenheit(user_degree)

print("\nResult:")
print(f"\tFahrenheit = {result}")
