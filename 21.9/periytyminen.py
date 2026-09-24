# class MyClass:
#     x = 1
#     y = 0

# p1 = MyClass()
# p2 = MyClass()
# p3 = MyClass()
# print(p1.x)
# print(p2.y)
# print(p3.x)
# del p1

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def greet(name, age):
        print(f"My name is {name} and i'm {age}")

p1 = Person('John', 36)
Person.greet(p1.name, p1.age)
