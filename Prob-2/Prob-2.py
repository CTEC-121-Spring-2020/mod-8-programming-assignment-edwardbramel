# Module 8
#   Programming Assignment 11
#     Prob-2.py

# Your code below
'''text
Name            ID Number       Major           GPA
Joe Bella       9933            Web Development 3.8
Tucker Blank    3399            Nursing         3.0
Gayle Ujifusa   1011            Baking          2.8
Edna Anker      9875            Medical Office  3.0
'''

'''
class student:
    def __init__(self, name, ID, major, GPA):
        self.name = name
        self.ID = ID
        self.major = major
        self.GPA = GPA

    def getID(self):
        return self.ID

    def SetID(self, ID):
        self.ID = ID


def main():
    # Joe = student("Joe Bella", "9933", "Web Dev", "3.8")
    # print(Joe)

    Joe = student("Joe Bella", "9933")
    print(Joe.name)

    # Joe.SetID("joe", "9933")
    # print("joes id is:", Joe.getID())
'''


class Student:
    def __init__(self, name, ID, major, GPA):
        self.name = name
        self.ID = ID
        self.major = ""
        self.GPA = 0.0

    def setname(self, name):
        self.name = name

    def getname(self):
        return self.name

    def setID(self, ID):
        self.ID = ID

    def getID(self):
        return self.ID

    def setmajor(self, major):
        self.major = major

    def getmajor(self):
        return self.major

    def setGPA(self, GPA):
        self.GPA = GPA

    def getGPA(self):
        return self.GPA


def test():
    studentlist = []
    studentlist.append(Student("Joe Bella", "9933", "web dev", "3.8"))
    studentlist.append(Student("Tucker", "3399", "nursing", "3.0"))
    studentlist.append(Student("Gayle Ujifusa", "1011", "baking", "2.8"))
    studentlist.append(Student("Edna Anker", "9875", "medical office", "3.0"))

    studentlist[0].setmajor("Web Dev")
    studentlist[1].setmajor("Nursing")
    studentlist[2].setmajor("Baking")
    studentlist[3].setmajor("Medical Office")

    studentlist[0].setGPA("3.8")
    studentlist[1].setGPA("3.0")
    studentlist[2].setGPA("2.8")
    studentlist[3].setGPA("3.0")

    for element in studentlist:
        print(element.getname())
        print(element.getID())
        print(element.getmajor())
        print(element.getGPA())


if __name__ == "__main__":
    test()
