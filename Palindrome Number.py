
 #Program to check if a number or string is a palindrome

def is_palindrome(value):
    # Convert value to string to handle both numbers and strings
    value_str = str(value)
    # Check if the string is equal to its reverse
    return value_str == value_str[::-1]

# Input the value (number or string)
value = input("Enter a number or a string: ")

# Check and print the result
if is_palindrome(value):
    print(f"{value} is a palindrome.")
else:
    print(f"{value} is not a palindrome.")