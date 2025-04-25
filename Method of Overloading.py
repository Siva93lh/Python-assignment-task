
#Method Overloading

# Write two methods with the same name but different number of parameters of same type

class MathOperations:
    # Method with two parameters
    def add_numbers(self, a, b):
        return a + b

    # Method with three parameters
    def add_numbers(self, a, b, c):
        return a + b + c

# Create an object of the MathOperations class
math_ops = MathOperations()

# Calling the method with two parameters (this will call the second method defined)
result = math_ops.add_numbers(5, 10, 15)
print(f"Sum of three numbers: {result}")


class MathOperations:
    # Method with two or three parameters using default values
    def add_numbers(self, a, b, c=0):  # c has a default value of 0
        return a + b + c

# Create an object of the MathOperations class
math_ops = MathOperations()

# Calling the method with two parameters
result1 = math_ops.add_numbers(5, 10)  # Only two arguments passed
print(f"Sum of two numbers: {result1}")

# Calling the method with three parameters
result2 = math_ops.add_numbers(5, 10, 15)  # Three arguments passed
print(f"Sum of three numbers: {result2}")


