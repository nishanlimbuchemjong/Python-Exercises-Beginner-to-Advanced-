"""
All Questions related to 'Tuples in Python'
"""
# Q.1) Given a tuple t = (10, 20, 30), unpack its values into three variables a, b, and c.
print("Question-1: Unpacking a Tuple:\n")

# kinitializing tuple 't'
t = (10, 20, 30)

# unpacking the tuple 't' into three variables a, b, and c
a, b, c = t

# printing the result after unpacking the tuple t
print(f"After unpacking the tuple t = ({t}) into three varibales a, b, and c, we get\n")
print(f" a = {a}")
print(f" b = {b}")
print(f" c = {c}")
print("````````````````````````````````````````````````````````````````````````````````\n")


# Q.2) Given a tuple t = (5, 1, 2, 5, 5, 3, 2), count the number of times 5 appears in the tuple.
print("\nQuestion-2: Count Elements\n")

# initializing tuple 't' as a varibale
t = (5, 1, 2, 5, 5, 3, 2)

# initializing the value of c'ount' variable
count = 0
for i in range(len(t)):
    if t[i] == 5:
        count += 1
    
print(f"Total count of 5 in tuple t= {t} is {count}")
print("````````````````````````````````````````````````````````````````````````````````\n")


# Q.3)Create a nested tuple: ((13, 23, 32), ("A", "B", "C"), ('a', 'b', 'c')). Access the second element of the first inner tuple and print it.
print("\nQuestion-3: Nested Tuple\n")

# initializing tuple 't' as a varibale
nested_tuple = ((13, 22, 33), ("A", "B", "C"), ('a', 'b', 'c'))

# unpacking the tuple 'nested_tuple' into three variables first_tuple, second_tuple, and third_tuple
first_tuple, second_tuple, third_tuple = nested_tuple

# printing the second element of the first tuple from the nested tuple
print(f"Second element of the first tuple i.e. ({first_tuple}), from the nested tuple i.e. ({nested_tuple}) is {first_tuple[1]}")
print("```````````````````````````````````````````````````````````````\n")


# Q.4) Create a tuple containing the squares of numbers from 1 to 10.
print("\nQuestion-4: CTuple of Squares\n")

# creating empty list
list_of_numbers = []
squared_list = []

# finding out all the numbers from 1 to 10 and then adding on the list i.e. list_of_numbers
for i in range(1, 10+1):
    list_of_numbers.append(i)

# findind out all the squares of a numbers and adding on the list i.e. squared_list
for i in list_of_numbers:
    if i**2 in list_of_numbers:
        squared_list.append(i**2)    
    else:
        pass

# converting the squared list into tuple
squared_tuple = tuple(squared_list)

# printing the tuple that only contains the square of numbers
print(f"\nNumbers from 1 to 10: {list_of_numbers}\n")
print(f"Required Tuple = {squared_tuple}")
print("```````````````````````````````````````````````\n")