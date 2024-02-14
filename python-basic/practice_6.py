# Define a class called Person
class Person:
  # Define the constructor method with attributes name, last_name, and age
  def __init__ (self, name, last_name, age):
    self.name = name
    self.last_name = last_name
    self.age = age
  
  # Define a method called sayHello
  def sayHello (self):
    # Print a message with the person's data
    print(f'Hello, my name is {self.name} {self.last_name} and I am {self.age} years old')

# Create an instance of the Person class with name "nei", last_name "villa", and age 26
nei = Person("nei", "villa", 26)
# Call the sayHello method of the nei instance
nei.sayHello()

# Define a class called Animal
class Animal:
  # Define the constructor method with attribute name
  def __init__ (self, name):
    self.name = name

  # Define a method called speak (to be overridden by subclasses)
  def speak (self):
    # Raise a NotImplementedError if called directly on the Animal class
    raise NotImplementedError
  
# Define a subclass called Dog, inheriting from the Animal class
class Dog (Animal):
  # Override the speak method
  def speak (self):
    # Print a message with the dog's name
    print(f'{self.name} says woof!')

# Define a subclass called Cat, inheriting from the Animal class
class Cat (Animal):
  # Override the speak method
  def speak (self):
    # Print a message with the cat's name
    print(f'{self.name} says meow!')

# Create an instance of the Dog class with name "Fido"
fido = Dog("Fido")
# Call the speak method of the fido instance
fido.speak()

# Create an instance of the Cat class with name "copito"
copito = Cat("copito")
# Call the speak method of the copito instance
copito.speak()

# Exercise 6: write a program that define a persona class with the attributes name, last_name and age. 
# The class should have a method sayHello that print a meggase with the data of the person.

class Person:
  def __init__ (self, name, last_name, age):
    self.name = name
    self.last_name = last_name
    self.age = age
  
  def sayHello (self):
    print(f'Hello, my name is {self.name} {self.last_name} and I am {self.age} years old')

nei = Person("nei", "villa", 26)
nei.sayHello()

