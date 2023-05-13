class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def say_hello(self):
        print(f"Hello, my name is {self.name} and I'm {self.age} years old.")

# Create an object of the Person class
person1 = Person("Alice", 25)

# Access object attributes
print(person1.name)  # Output: Alice
print(person1.age)   # Output: 25

# Call object methods
person1.say_hello()  # Output: Hello, my name is Alice and I'm 25 years old.

# Note " : " you must follow this indentation and four spaces