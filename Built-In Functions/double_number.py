# Use the map() function to double the numbers in the list [1, 2, 3, 4, 5].

number_list =  [1, 2, 3, 4, 5]

# calculating the double of the numbers in given list using map() built-in functions
result = list(map(lambda x: x*2, number_list))

# printing the result
print(f"Double the numbers in the list {number_list} are: {result}")