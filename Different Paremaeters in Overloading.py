
#Method Overloading

#2. Write two methods with the same name but different number of parameters of different

class Operations:
    # Method that accepts two integers
    def process_data(self, a, b):
        if isinstance(a, int) and isinstance(b, int):
            return a + b
        else:
            print("Error: Both parameters should be integers.")

    # Method that accepts two strings
    def process_data(self, a, b):
        if isinstance(a, str) and isinstance(b, str):
            return a + " " + b
        else:
            print("Error: Both parameters should be strings.")

# Create an object of the Operations class
ops = Operations()

# Calling the method with two integers
result_int = ops.process_data(5, 10)  # This should call the integer version
print(f"Sum of integers: {result_int}")

# Calling the method with two strings
result_str = ops.process_data("Hello", "World")  # This should call the string version
print(f"Concatenated string: {result_str}")



class Operations:
    # Single method that processes both integers and strings
    def process_data(self, a, b):
        if isinstance(a, int) and isinstance(b, int):
            return a + b  # Sum of integers
        elif isinstance(a, str) and isinstance(b, str):
            return a + " " + b  # Concatenation of strings
        else:
            return "Error: Invalid argument types. Must be both integers or both strings."

# Create an object of the Operations class
ops = Operations()

# Calling the method with two integers
result_int = ops.process_data(5, 10)
print(f"Sum of integers: {result_int}")

# Calling the method with two strings
result_str = ops.process_data("Hello", "World")
print(f"Concatenated string: {result_str}")

# Calling the method with invalid argument types
result_invalid = ops.process_data(5, "Hello")
print(result_invalid)


