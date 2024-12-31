"""
All Question related to 'Dictionaries in Python'
"""
# Q.1) Write a program to check if the key "Projects" exists in the dictionary {"Name": "AI Engineer", "Experience": 2}.

print("Question-1: Check if Key Exists\n")

# initializing the dictionary
personal_profile = {"Name": "AI Engineer", "Experience": 2}

# checking if the key "Projects" exists in the given dictionary and printing the result
print("Result:")
if 'Projects' in personal_profile:
    print(f"\n'Project' key exists in dictionary '{personal_profile}'")
else:
    print(f"\n'Project' key does not exist in dictionary '{personal_profile}'")


print("````````````````````````````````````````````````````````````\n")


"""
Q.2) Create a dictionary representing an AI engineer's profile:
    profile = {
        "Name": "John",
        "Skills": {"Programming": ["Python", "C++"], "AI": ["ML", "DL"]},
        "Experience": {"Years": 5, "Projects": 10}
    }
    Access and print the "Programming" skills.
"""
print("Question-2: Nested Dictionary\n")

# initializing the dictionary 'profile'
profile = {
    "Name": "Nishan",
    "Skills": {"Programming": ["Python", "C++"], "AI": ["ML", "DL"]},
    "Experience": {"Years": 2, "Projects": 6}
}

# accessing the programming skills 
programming_names = profile['Skills']['Programming']

# printing the result
print(f"\nProfile dictionary is given below:")
print(profile)
print("\nThe programming skills are given below:")
for i in programming_names:
    print(i)
print("````````````````````````````````````````````````````````````\n")
