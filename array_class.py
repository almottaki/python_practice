# cars = ["Ford", "Volvo", "BMW"]
# x = cars[0]
# cars[0] = "Toyota"
# print(cars)
# y = len(cars)
# print(y)
# for x in cars:
#   print(x)
#
# cars.append("Honda")
# print(cars)
# cars.pop(1)
# print(cars)
# cars.remove("BMW")
# print(cars)

# class MyClass:
#   x = 5
# # p1 = MyClass()
# print(MyClass.x)

# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age
#
# p1 = Person("Mottaki", 21)
#
# print(p1.name)
# print(p1.age)


# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age
#
#   def myfunc(self):
#     print("Hello! My name is " + self.name)
#
# p1 = Person("John", 36)
# p1.myfunc()

# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age
#
#   def __str__(self):
#     return f"{self.name}({self.age})"
#
# p1 = Person("John", 36)
#
# print(p1)


# class Person:
#   def __init__(mysillyobject, name, age):
#     mysillyobject.name = name
#     mysillyobject.age = age
#
#   def myfunc(abc):
#     print("Hello my name is " + abc.name)
#
# p1 = Person("John", 36)
# p1.name = "Smith"
# del p1.age
# p1.myfunc()


# class Person:
#   def __init__(self, fname, lname):
#     self.firstname = fname
#     self.lastname = lname
#
#   def printname(self):
#     print(self.firstname, self.lastname)


# x = Person("John", "Doe")
# x.printname()


# cars = ["Ford", "Volvo", "BMW"]
# bus = ["ac", "ascsa", "ascsa"]
# print(cars+bus)
# print(cars)