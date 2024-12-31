# Write a function is_palindrome that checks whether a given string is a palindrome.

def is_palindrome(number):
    # reversing the original number
    rev_number = number[::-1]

    # checking that the original number and the reversed number are equal or not
    if rev_number == number:
        return True
    else:
        return False

# taking users number
num = input("Enter your number: ")

# calling the is_palondrome() function
result = is_palindrome(num)

print("\nResult:")
# checking is_palindrome() function is returning True or False and printing the result
if result == True:
    print(f"\t{num} is a palindrome number.")
else:
    print(f"\t{num} is not a palindrome number.")
