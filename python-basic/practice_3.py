def sum(a, b):
  return a + b

result = sum(10, 20)

print("sum of a and b: ", result)

def greetings(name, last_name = "Smith"):
  return "Hello {} {}".format(name, last_name)

print(greetings("John"))
print(greetings("John", "Doe"))

def sum_rest(a, b):
  return a + b, a - b

sum_result, rest_result = sum_rest(10, 20)

print("sum of a and b: ", sum_result)
print("rest of a and b: ", rest_result)

help(sum)

# Exercise 3: create a funtion that calculates the area of a circle
# The formula is: area = pi * r^2
# Use the math module to get the value of pi
# Use the input function to get the value of r
def area_of_circle(r):
  import math
  return math.pi * r ** 2

area = area_of_circle(10)

print("Area of the circle: ", area)
