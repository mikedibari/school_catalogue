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
print(a)
print(a.getName())
print(a.getLevel())
a.setNumberOfStudents(400)
print(a.getNumberOfStudents())

b = PrimarySchool("Boston Elementary", 500, "'Pickup Allowed'")
print(b.getPickupPolicy())
print(b)

c = HighSchool("Medford High", 250, ["Football", "Baseball", "Lacrosse"])
print(c.getSportsTeams())
print(c)
