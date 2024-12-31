"""
Write a function celsius_to_fahrenheit that takes a temperature in Celsius and converts it to Fahrenheit.
Formula: F = (C X 9/5) + 32
"""

# a funciton to calculate the fahrenheit
def celsius_to_fahrenheit(degree):
    return degree * (9 / 5) + 32

# taking a degree celsius from the user
user_degree = float(input("Enter a degree celsius: "))

# call the function
result = celsius_to_fahrenheit(user_degree)

# printing the result
print("\nResult:")
print(f"\tFahrenheit = {result}")