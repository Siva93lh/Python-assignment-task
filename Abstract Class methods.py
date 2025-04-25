
#Abstract Class
#. Create an abstract class with abstract and non-abstract methods.

from abc import ABC, abstractmethod

# Creating an abstract class
class MyAbstractClass(ABC):

    # Abstract method (no implementation here)
    @abstractmethod
    def abstract_method(self):
        pass

    # Non-abstract method (with implementation)
    def non_abstract_method(self):
        print("This is a non-abstract method with implementation.")

# Creating a subclass of the abstract class
class MyConcreteClass(MyAbstractClass):
    # Implementing the abstract method
    def abstract_method(self):
        print("This is the implementation of the abstract method.")

# Trying to create an object of the abstract class will result in an error
# abstract_obj = MyAbstractClass()  # This will raise a TypeError: Can't instantiate abstract class

# Creating an object of the subclass which implements the abstract method
concrete_obj = MyConcreteClass()

# Calling both abstract and non-abstract methods
concrete_obj.abstract_method()  # This will call the implemented abstract method
concrete_obj.non_abstract_method()  # This will call the non-abstract method