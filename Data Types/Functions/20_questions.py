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
