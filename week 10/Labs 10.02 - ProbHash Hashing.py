"""Lab 10.02 - ProbHash Hashing.py"""
from json import loads as l

class Student:
    """-"""
    def __init__(self, std_id=0, name="", gpa=0.0):
        """-"""
        self.__std_id = int(std_id)
        self.__name = str(name)
        self.__gpa = float(gpa)

    def get_std_id(self):
        """-"""
        return int(self.__std_id)

    def get_name(self):
        """-"""
        return str(self.__name)

    def get_gpa(self):
        """-"""
        return float(self.__gpa)

    def print_details(self):
        """-"""
        print("ID: %d\nName: %s\nGPA: %.02f" %(self.get_std_id(), self.get_name(), self.get_gpa()))

class ProbHash:
    """-"""
    def __init__(self, size):
        """-"""
        self.__size = size
        self.__hash_table = [[] for _ in range(size)]

    def hash(self, key):
        """-"""
        keys = key % self.__size
        if self.__hash_table[keys] == []:
            return int(keys)
        else:
            return self.hash(self.rehash(key))

    def rehash(self, key):
        """-"""
        return int(key + 1) % self.__size

    def insert_data(self, student):
        """-"""
        if [] in self.__hash_table:
            keys = self.hash(student.get_std_id())
            self.__hash_table[keys] = student
            print("Insert %d at index %d" % (student.get_std_id(), keys))
        else:
            print("The list is full. %d could not be inserted." % (student.get_std_id()))

    def search_data(self, std_id):
        """-"""
        keys = std_id % self.__size
        count = 0
        while self.__hash_table[keys] != [] and self.__hash_table[keys].get_std_id() != std_id\
        and count <= self.__size:
            keys = self.rehash(keys)
            count += 1
        if self.__hash_table[keys] != [] and self.__hash_table[keys].get_std_id() == std_id:
            print("Found %d at index %d" % (std_id, keys))
            return self.__hash_table[keys]
        else:
            print("%d does not exist." % std_id)
            return None

def main():
    """-"""
    size = int(input())
    hashtable = ProbHash(size)
    while True:
        finish = input()
        if finish == "Done":
            break
        condition, data = finish.split(" = ")
        if condition == "I":
            std_in = l(data)
            std = Student(std_in["ID"], std_in["Name"], std_in["GPA"])
            hashtable.insert_data(std)
        elif condition == "S":
            print("------")
            student = hashtable.search_data(int(data))
            if student is not None:
                student.print_details()
            print("------")
        else:
            print("Invalid Condition!")
main()
