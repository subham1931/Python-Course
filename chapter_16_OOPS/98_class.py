class Student:
    ##init was a cunstructor
    def __init__(self,name,roll,cgpa):
        ##creating instance veriable
        print('constructor called')
        self.name=name
        self.roll = roll
        self.cgpa = cgpa

s1 = Student('subham',27,7.95)
s2 = Student('Rohit',28,9.95)

print(s1.name)