"""Exercise 00.04 - Person V.1"""

class Person:
    """-"""
    def __init__(self, name, age):
        """-"""
        self.name = name
        self.age = age

        self.get_details()
        self.say_hello()

    def get_details(self):
        """-"""
        print("%s, %s years old" % (self.name, self.age))

    def say_hello(self):
        """-"""
        print("Hello, my name is %s!" % (self.name))

Person(input(), input())
