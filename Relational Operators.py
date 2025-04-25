
def relational_operators(a, b):
    print(f"{a} < {b}: {a < b}")   
    print(f"{a} <= {b}: {a <= b}")
    print(f"{a} > {b}: {a > b}")   
    print(f"{a} >= {b}: {a >= b}") 

# Input two numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Demonstrate relational operators
relational_operators(num1, num2)