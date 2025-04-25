
# Class with constructor initializing attributes
class Person:
    # Constructor to initialize attributes
    def __init__(self, name, age, city):
        # Initialize the attributes
        self.name = name
        self.age = age
        self.city = city

    # Method to display the person's information
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"City: {self.city}")

# Create an object of Person class and initialize attributes via the constructor
person1 = Person("Alice", 30, "New York")

# Call the display_info method to print the object's attributes
person1.display_info()

# Create another object with different attributes
person2 = Person("Bob", 25, "Los Angeles")

# Call the display_info method for the second object
person2.display_info()
