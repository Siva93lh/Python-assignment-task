
#2. Create a class with PROTECTED fields and methods. Access these fields and methods
#from any other class in the same package.
# Also, Access the PROTECTED fields and methods from child class located in a different package
#Access the PROTECTED fields and methods from any class in different package.


class MyBaseClass:
    def __init__(self):
        self._protected_field = "This is a protected field"  # Protected field

    def _protected_method(self):
        print("This is a protected method.")

class MySubClass(MyBaseClass):
    def __init__(self):
        super().__init__()

    def access_protected(self):
        print(self._protected_field)  # Accessing protected field from subclass
        self._protected_method()  # Calling protected method from subclass

# Creating an object of MySubClass and accessing protected members
sub_obj = MySubClass()
sub_obj.access_protected()

# Accessing protected members directly from outside the class (not recommended, but possible)
base_obj = MyBaseClass()
print(base_obj._protected_field)  # Accessing protected field from outside
base_obj._protected_method()  # Calling protected method from outside