
# Program to check if a number is an Armstrong number

def is_armstrong_number(num):
    # Convert the number to string to find the number of digits
    num_str = str(num)
    num_digits = len(num_str)
    
    # Calculate the sum of each digit raised to the power of num_digits
    sum_of_digits = sum(int(digit) ** num_digits for digit in num_str)
    
    # Check if the sum is equal to the original number
    if sum_of_digits == num:
        return True
    else:
        return False

# Input the number to check
number = int(input("Enter a number: "))

# Check and print the result
if is_armstrong_number(number):
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")