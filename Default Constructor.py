
#CONSTRUCTORS

# Write a class with a default constructor, one argument constructor and two argument
#constructors. Instantiate the class to call all the constructors of that class from a main

class MyClass:
    # Default constructor
    def __init__(self, arg1=None, arg2=None):
        if arg1 is None and arg2 is None:
            print("Default constructor called.")
        elif arg2 is None:
            print(f"One-argument constructor called with arg1 = {arg1}.")
        else:
            print(f"Two-argument constructor called with arg1 = {arg1} and arg2 = {arg2}.")

# Main class or main method
if __name__ == "__main__":
    # Instantiate the class to call the default constructor
    obj1 = MyClass()

    # Instantiate the class to call the one-argument constructor
    obj2 = MyClass("Argument1")

    # Instantiate the class to call the two-argument constructor
    obj3 = MyClass("Argument1", "Argument2")




