"""
Store your first name, last name, and age in separate variables. Combine them into a single variable as a formatted string, e.g., "John Doe, Age: 25".

"""
name = "Nishan Limbu"
age = "23"
student_detail = ", Age = ".join([name, age])
print(f"{student_detail}")