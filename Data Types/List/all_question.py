# Q.1) Create a list of the first 10 even numbers.
print("Question-1: \n")
# initializing the list
even_list = []

# finding out the first 10 even numbers using for-loop
for i in range(1, 21):
    if i%2 == 0:
        even_list.append(i) # storing the even numbers in the list

# printing out the list
print(f"List: {even_list}")
print("................................................................\n")
