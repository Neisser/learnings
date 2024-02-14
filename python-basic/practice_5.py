# Import the 'math' module
import math

# Print the value of pi from the 'math' module
print(math.pi)

# Print the list of attributes and functions in the 'math' module
print(dir(math))

# Import the 'practice_5_math' module
import practice_5_math

# Print the list of attributes and functions in the 'practice_5_math' module
print(dir(practice_5_math))

# Print the help documentation for the 'practice_5_math' module
print(help(practice_5_math))

# Import the 'person' class from the 'practice_5_person' module
from practice_5_person import person

# Import specific functions from the 'practice_5_math' module
from practice_5_math import add, subtract, multiply, divide

# Create an instance of the 'person' class with name "John" and age 36
person1 = person("John", 36)

# Call the 'sayHello' method of the 'person1' instance
person1.sayHello()

# Call the 'add' function from the 'practice_5_math' module with arguments 5 and 3
print(add(5, 3))

# Call the 'subtract' function from the 'practice_5_math' module with arguments 5 and 3
print(subtract(5, 3))

# Call the 'multiply' function from the 'practice_5_math' module with arguments 5 and 3
print(multiply(5, 3))

# Call the 'divide' function from the 'practice_5_math' module with arguments 5 and 3
print(divide(5, 3))


# Exercise 5: write a program that generates a random number between 1 and 100
import random

print(random.randint(1, 100))

# print(help(random))


