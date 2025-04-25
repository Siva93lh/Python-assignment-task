#1. Create a class with PRIVATE fields, private method and a main method. Print the fields
# main method. #Call the private method in main method.
#Create a sub class and try to access the private fields and methods from sub class.

class MyClass:
    def __init__(self):
        self.__private_field = "This is a private field"  # Private field
        self.__private_field_2 = "Another private field"  # Another private field

    def __private_method(self):
        print("This is a private method.")

    def main(self):
        print(self.__private_field)  # Accessing private field in main method
        print(self.__private_field_2)  # Accessing another private field
        self.__private_method()  # Calling private method

# Creating an object of MyClass and calling the main method
obj = MyClass()
obj.main()

# Attempt to access private fields or methods outside the class (this will raise an error)
# print(obj.__private_field)  # This will raise an AttributeError
# obj.__private_method()  # This will raise an AttributeError
class MySubclass(MyClass):
    def __init__(self):
        super().__init__()

    def access_private(self):
        # This will raise an AttributeError because private members are not accessible from subclass
        # print(self.__private_field)  # This will raise AttributeError
        pass

# Creating a subclass object
sub_obj = MySubclass()
sub_obj.access_private()  # Trying to access private members
