"""Exercise 00.04 - Person V.1"""

class Person:
    """-"""
    def __init__(self, name, age):
        """-"""
        self.name = name
        self.age = age

        # self.get_details()
        # self.say_hello()

    def get_details(self):
        """-"""
        print("%s, %s years old" % (self.name, self.age))

    def say_hello(self):
        """-"""
        return "Hello, my name is %s!" % (self.name)

class Project:
    """-"""
    def __init__(self, projectname, num_members):
        """-"""
        self.projectname = projectname
        self.num_members = num_members

        self.showprojectname()
        self.showmember()

    def showprojectname(self):
        """-"""
        print("Hello There! This is %s" % self.projectname)

    def showmember(self):
        """-"""
        print("This project has %s members" % self.num_members)

def main(name, jumnuan):
    """-"""
    storage = []
    Project(name, jumnuan)
    for _ in range(jumnuan):
        person = Person(input(), input())
        storage.append(person.say_hello())
    storage.sort()
    print(*storage, sep='\n')

main(input(), int(input()))
