
# Global variable
my_var = "I am a global variable"

def my_function():
    # Local variable
    my_var = "I am a local variable"
    print("Inside the function, my_var:", my_var)  # This will use the local variable

# Print the global variable
print("Outside the function, my_var:", my_var)

# Call the function
my_function()

# Print the global variable again to show it remains unchanged
print("Outside the function after calling it, my_var:", my_var)