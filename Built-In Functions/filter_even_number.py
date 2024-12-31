# Use the filter() function to extract only even numbers from the list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = list(filter(lambda x: x % 2 == 0, number_list))
# filterig the even number from list using filter() built-in function
print(f"Even Numbers from list {number_list} are:{result}")

    