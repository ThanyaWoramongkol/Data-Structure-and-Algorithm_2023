"""Labs 10.01 - Student Class.py"""

class Student:
    """-"""
    def __init__(self, std_id=None, name=None, gpa=None):
        """Constuctor"""
        if std_id == None and name == None and gpa == None:
            self.__std_id = 0
            self.__name = ""
            self.__gpa = 0.0
        else:
            self.__std_id = std_id
            self.__name = name
            self.__gpa = gpa

    def get_sta_id(self):
        """-"""
        return self.__std_id

    def get_name(self):
        """-"""
        return self.__name

    def get_gpa(self):
        """-"""
        return self.__gpa

    def print_detail(self):
        """-"""
        print("ID: %d\nName: %s\nGPA: %.2f" % (self.__std_id, self.__name, self.__gpa))

def main(text_in):
    """-"""
    from json import loads as l
    std_in = l(text_in)
    std = Student(std_in["ID"], std_in["Name"], std_in["GPA"])
    std.print_detail()
main(input())
