
#Packages

# class_package/class1.py
class Class1:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, {self.name}! Welcome to Class1.")

# class_package/class2.py
class Class2:
    def __init__(self, age):
        self.age = age

    def show_age(self):
        print(f"You are {self.age} years old in Class2.")

class Class1:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, {self.name}! Welcome to Class1.")


class Class1:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, {self.name}! Welcome to Class1.")

class Class2:
    def __init__(self, age):
        self.age = age

    def show_age(self):
        print(f"You are {self.age} years old in Class2.")


# Creating objects for each class
obj1 = Class1("John")
obj2 = Class2(25)

# Calling methods of each class
obj1.greet()
obj2.show_age()