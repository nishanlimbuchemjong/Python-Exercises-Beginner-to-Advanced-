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


# Q.2) Write a program to find the largest and smallest numbers in a list.
print("Question-2: \n")
number_list = [13, 43, 56, 34, 2, 4, 30, 22, 45, 77, 75]

largest_num = max(number_list)
smallest_num = min(number_list)

print(f"Largest number: {largest_num}")
print(f"Smallest number: {smallest_num}")
print("................................................................\n")
