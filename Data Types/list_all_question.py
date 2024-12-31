"""
All Questions related to 'List in Python'
"""
# Q.1)Given the list nums = [10, 20, 30, 40], write a program to reverse its order.

print("Question-1: Reverse a List\n")

# initializing the list 'nums'
nums = [10, 20, 30, 40]

print(f"Before reversing the list {nums}\n")
# sorting all numbers in descenting
nums.sort(reverse=True)

# printing the result after reversing
print(f"After reversing the order of the list: {nums}")
print("````````````````````````````````````````````````````\n")


# Q.2)Given a list of integers nums = [10, 20, 30, 40, 50], write a program to find and print the maximum and minimum values.
print("Question-2: Find Maximum and Minimum\n")

# initializing the list
nums = [10, 60, 30, 40, 50]

# first, sorting the list in ascending order
nums.sort()

# accessing the maximum and minimum value in the list and printing the result
print(f"Given list = {nums}\n")
print(f"Result:\n\tMaximum = {nums[-1]}")
print(f"\tMinimum = {nums[0]}")
print("``````````````````````````````````\n")

# Q.3) Write a program to check if the number 25 exists in the list nums = [10, 20, 30, 40, 50]
print("Question-3: Check Membership\n")

# initializing the list:
nums = [10, 20, 30, 40, 50]
given_num = 25
# checking the number 25 exists in list 'nums' or not
if given_num in nums:
    print(f"{given_num} exist in {nums}")
else:
    print(f"{given_num} does not exist in {nums}")

print("`````````````````````````````\n")

# Q.4) Write a program to count how many times the number 2 appears in the list nums = [11, 22, 22, 33, 44, 22].
print("Question-4: Count Element Occurrences")

# initializing the list
nums = [11, 22, 22, 33, 44, 22]
apppear_num = 22
count = 0

for i in range(len(nums)):
    if apppear_num in nums:
        if nums[i] == apppear_num:
            count += 1
        else:
            pass
    else:
        pass

print(f"Given list = {nums}\n")
print(f"Result:\n\tTotal Occurrences of {apppear_num} = {count}")
print("```````````````````````````````````````````````````````````\n")