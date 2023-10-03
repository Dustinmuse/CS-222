class Student:
    numberOfStudents = 0 #class variable
    def __init__(self, firstName, lastName): #init is the constructor
        self.firstName = firstName #static variable
        self.lastName = lastName #static variable

    def printStudent(self):
        print(self.lastName + ", " + self.firstName)

    @classmethod #can minipulate the class variables
    def updateStudents(cls):
        cls.numberOfStudents += 1

alice = Student("Alice", "Jones")
Student.updateStudents()
bob = Student("Bob", "Smith")
Student.updateStudents()
print(alice.numberOfStudents)
print(bob.numberOfStudents)
print(Student.numberOfStudents)