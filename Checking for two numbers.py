
def check_equality(num1, num2):
    if num1 == num2:
        return "The two numbers are equal."
    else:
        return "The two numbers are not equal."

# Input two numbers
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

# Check equality and print the result
result = check_equality(number1, number2)
print(result)
