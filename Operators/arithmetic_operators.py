"""
Implement a program to check if two given integers are equal, not equal, or one is greater than the other using relational operators.
"""
# initializing the values of x and y
x, y = 50, 60


print(f"x = {x} and y = {y}\nResults:")

# checking the different conditions
if x == y:
    print("x is equal to y")
elif x != y:
    print("x is not equal to y")
    print("Also,")
    if x > y:
        print("x is greater to y")
    else:
        print("y is greater to x")
else:
    pass

