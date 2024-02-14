class person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def sayHello(self):
    print("Hello, my name is {} {}".format(self.name, self.age))

__all__ = ["person"]