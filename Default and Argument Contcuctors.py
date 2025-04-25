
#Call the constructors(both default and argument constructors) of super class from a child

class SuperClass:
    # Default constructor
    def __init__(self, arg1=None, arg2=None):
        if arg1 is None and arg2 is None:
            print("SuperClass default constructor called.")
        elif arg2 is None:
            print(f"SuperClass one-argument constructor called with arg1 = {arg1}.")
        else:
            print(f"SuperClass two-argument constructor called with arg1 = {arg1} and arg2 = {arg2}.")

# Child class that calls the constructors of SuperClass
class ChildClass(SuperClass):
    def __init__(self, arg1=None, arg2=None):
        # Calling the SuperClass default constructor
        super().__init__()

        # Calling the SuperClass one-argument constructor
        if arg1 is not None and arg2 is None:
            super().__init__(arg1)

        # Calling the SuperClass two-argument constructor
        elif arg1 is not None and arg2 is not None:
            super().__init__(arg1, arg2)

# Instantiate the ChildClass and call the constructors
print("Child object 1:")
child1 = ChildClass()  # Calls SuperClass default constructor

print("\nChild object 2:")
child2 = ChildClass("Argument1")  # Calls SuperClass one-argument constructor

print("\nChild object 3:")
child3 = ChildClass("Argument1", "Argument2")  # Calls SuperClass two-argument constructor



