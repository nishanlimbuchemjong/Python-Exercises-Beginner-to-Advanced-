# Write a function is_prime that takes a number and returns True if the number is prime, and False otherwise.

def is_prime(num):
    if num > 3:
        if (num % 2 == 0) or (num % 3 == 0):
            return False
        else:
            return True
    else:
        if num == 1:
            return False
        else:
            return True
    
number = int(input("Enter a number: "))

result = is_prime(number)

# printing the result
print("Here,\n\t'True' ---> Prime Number")
print("\n\t'False' ---> Not a Prime Number")
print(f"\nResult: {result}\n\n")