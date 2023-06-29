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
        return f'A {self.level} school named {self.name} with {self.numberOfStudents} students.'
# inherits from School
class PrimarySchool(School):
    def __init__(self, name, numberOfStudents, pickupPolicy):
        super().__init__(name, "primary", numberOfStudents)
        self.pickupPolicy = pickupPolicy

    def getPickupPolicy(self):
        return self.pickupPolicy

    def __repr__(self):
        # use super() to avoid repeating code
        parentRepr = super().__repr__()
        return parentRepr + f' The pickup policy is {self.pickupPolicy}.'

class HighSchool(School):
    def __init__(self, name, numberOfStudents, sportsTeams):
        super().__init__(name, "high", numberOfStudents)
        self.sportsTeams = sportsTeams

    def getSportsTeams(self):
        return self.sportsTeams
    # override to display sportsTeams
    def __repr__(self):
        parentRepr = super().__repr__()
        return parentRepr + f' The sports teams are {self.sportsTeams}.' 

a = School("Cambridge", "high", 300)
print(a) # A high school named Cambridge with 300 students.
print(a.getName()) # Cambridge
print(a.getLevel()) # high
a.setNumberOfStudents(400) # calls setter method
print(a.getNumberOfStudents()) # 400

b = PrimarySchool("Boston Elementary", 500, "'Pickup Allowed'")
print(b.getPickupPolicy()) # 'Pickup Allowed'
print(b) # A primary school named Boston Elementary with 500 students. The pickup policy is 'Pickup Allowed'.

c = HighSchool("Medford High", 250, ["Football", "Baseball", "Lacrosse"])
print(c.getSportsTeams()) # ['Football', 'Baseball', 'Lacrosse']
print(c) # A high school named Medford High with 250 students. The sports teams are ['Football', 'Baseball', 'Lacrosse'].
