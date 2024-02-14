# Define a function named 'sum' that takes two parameters 'a' and 'b'
def sum(a, b):
  # Return the sum of 'a' and 'b'
  return a + b

# Call the 'sum' function with arguments 10 and 20 and assign the result to 'result'
result = sum(10, 20)

# Print the string "sum of a and b: " followed by the value of 'result'
print("sum of a and b: ", result)

# Define a function named 'greetings' that takes two parameters 'name' and 'last_name' with a default value of "Smith"
def greetings(name, last_name = "Smith"):
  # Return a formatted string that greets the person with their name and last name
  return "Hello {} {}".format(name, last_name)

# Call the 'greetings' function with argument "John" and print the returned value
print(greetings("John"))

# Call the 'greetings' function with arguments "John" and "Doe" and print the returned value
print(greetings("John", "Doe"))

# Define a function named 'sum_rest' that takes two parameters 'a' and 'b'
def sum_rest(a, b):
  # Return a tuple containing the sum of 'a' and 'b' and the difference between 'a' and 'b'
  return a + b, a - b

# Call the 'sum_rest' function with arguments 10 and 20 and assign the returned values to 'sum_result' and 'rest_result' respectively
sum_result, rest_result = sum_rest(10, 20)

# Print the string "sum of a and b: " followed by the value of 'sum_result'
print("sum of a and b: ", sum_result)

# Print the string "rest of a and b: " followed by the value of 'rest_result'
print("rest of a and b: ", rest_result)

# Display the help documentation for the 'sum' function
help(sum)

# Define a function named 'area_of_circle' that takes one parameter 'r'
def area_of_circle(r):
  # Import the 'math' module
  import math
  # Return the area of the circle using the formula: area = pi * r^2
  return math.pi * r ** 2

# Call the 'area_of_circle' function with argument 10 and assign the returned value to 'area'
area = area_of_circle(10)

# Print the string "Area of the circle: " followed by the value of 'area'
print("Area of the circle: ", area)
