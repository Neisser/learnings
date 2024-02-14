age = int(input("Enter your age: "))

if age >= 18:
  print("You are an adult")
else:
  print("You are a minor")

for i in range(age):
  print(i)

# Exercise 4: create a function that print the numbers from 1 to 100 but only the even numbers

def even_numbers(top):
  for i in range(1, top):
    if i % 2 == 0:
      print(i)

top = int(input("Enter the top number: "))

even_numbers(top)