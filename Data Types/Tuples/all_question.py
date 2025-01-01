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