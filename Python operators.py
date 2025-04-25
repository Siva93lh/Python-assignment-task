
#Python operators

def arithmetic_operations(a, b, operator):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        if b != 0:
            return a / b
        else:
            return "Error: Division by zero is not allowed."
    else:
        return "Error: Invalid operator."

# Test the function
num1 = 10
num2 = 5

print("Addition (+):", arithmetic_operations(num1, num2, '+'))
print("Subtraction (-):", arithmetic_operations(num1, num2, '-'))
print("Multiplication (*):", arithmetic_operations(num1, num2, '*'))
print("Division (/):", arithmetic_operations(num1, num2, '/'))