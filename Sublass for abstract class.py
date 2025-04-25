# Create a sub class for an abstract class. Create an object in the child class for the
#abstract class and access the non-abstract methods
from abc import ABC, abstractmethod

# Abstract class with abstract and non-abstract methods
class MyAbstractClass(ABC):
    # Abstract method (no implementation here)
    @abstractmethod
    def abstract_method(self):
        pass

    # Non-abstract method (with implementation)
    def non_abstract_method(self):
        print("This is a non-abstract method with implementation.")

# Subclass of MyAbstractClass
class MyConcreteClass(MyAbstractClass):

    # Implementing the abstract method
    def abstract_method(self):
        print("This is the implementation of the abstract method.")

# Creating an object of the subclass
concrete_obj = MyConcreteClass()

# Calling the non-abstract method from the abstract class (inherited)
concrete_obj.non_abstract_method()

# Calling the implemented abstract method
concrete_obj.abstract_method()