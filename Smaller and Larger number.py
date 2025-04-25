
#Smaller and larger Number5

def find_smaller_and_larger(num1, num2):
    if num1 < num2:
        print(f"The smaller number is: {num1}")
        print(f"The larger number is: {num2}")
    elif num1 > num2:
        print(f"The smaller number is: {num2}")
        print(f"The larger number is: {num1}")
    else:
        print("Both numbers are equal.")

# Input two numbers
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

# Find and print the smaller and larger numbers
find_smaller_and_larger(number1, number2)