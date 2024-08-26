# Define a class named Person
class Person:
    # Constructor to initialize the object with name and age
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    # Method to display information about the person
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Creating objects of the Person class
person1 = Person("Alice", 30)
person2 = Person("Bob", 25)

# Accessing attributes and calling methods of objects
person1.display_info()  # Output: Name: Alice, Age: 30
person2.display_info()  # Output: Name: Bob, Age: 25
