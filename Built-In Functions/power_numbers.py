# Use the pow() function to calculate 2 raised to the power of 5.

def get_integer_number(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("\nInvalid number! Please enter an integer number\n")
        
number = get_integer_number("Enter a number: ")
power_of = get_integer_number("Enter a number as a power: ")

result = pow(number, power_of)

print(f"\nResult:\n\tPower of {number} raised to the power of {power_of} is {result}")