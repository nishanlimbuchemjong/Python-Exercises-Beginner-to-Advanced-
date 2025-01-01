# Q.1) Write a program to swap the first and last elements of a tuple.
print("Question-1:\n")
subjects = ("Science", "Mathematics", "English", "Optional Math", "Social")

first_element = subjects[0]
last_element = subjects[-1]

subjects_list = list(subjects)
subjects_list[0] = last_element
subjects_list[-1] = first_element
print(first_element)
print(last_element)
print(f"Before swapping the first and last element of a tuple, we get\n\t{subjects}")
print(f"After swapping the first and last element of a tuple, we get\n\t{tuple(subjects_list)}")
print(".................................................................\n")


# Q.2) Unpack the tuple `(10, 20, 30, 40)` into four variables and print them.
print("Question-2:")
a, b, c, d = (10, 20, 30, 40)

print("After upacking the tuple (10, 20, 30, 40), we get")
print(f" a = {a}")
print(f" b = {b}")
print(f" c = {c}")
print(f" d = {d}")
print(".......................................\n")