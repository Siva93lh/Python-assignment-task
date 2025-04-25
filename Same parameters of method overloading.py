#Method Overloading

# Write two methods with the same name and same number of parameters of same type

class Operations:
    # Method that processes integers (same number of parameters)
    def process_data(self, a, b):
        # First behavior: add the numbers if both are positive
        if a > 0 and b > 0:
            return a + b
        # Second behavior: subtract the numbers if both are negative
        elif a < 0 and b < 0:
            return a - b
        else:
            return

# Create an object of the Operations class
ops = Operations()

# Calling the method with two positive integers
result1 = ops.process_data(5, 10)
print(f"Result with positive numbers: {result1}")

# Calling the method with two negative integers
result2 = ops.process_data(-5, -10)
print(f"Result with negative numbers: {result2}")

# Calling the method with mixed positive and negative numbers
result3 = ops.process_data(5, -10)
print(f"Result with mixed numbers: {result3}")




