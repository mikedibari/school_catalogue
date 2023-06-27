class School():
    def __init__(self, name, level, numberOfStudents):
        self.name = name
        self.level = level
        self.numberOfStudents = numberOfStudents
    # getter methods
    def getName(self):
        return self.name

    def getLevel(self):
        return self.level

    def getNumberOfStudents(self):
        return self.numberOfStudents
    # setter method
    def setNumberOfStudents(self, newNumberOfStudents):
        self.numberOfStudents = newNumberOfStudents
    # return the string that's displayed when you print an object of the class
    def __repr__(self):
        return f'A {self.level} school named {self.name} with {self.numberOfStudents} students'

a = School("Cambridge", "high", 300)
print(a)
print(a.getName())
print(a.getLevel())
a.setNumberOfStudents(400)
print(a.getNumberOfStudents())
