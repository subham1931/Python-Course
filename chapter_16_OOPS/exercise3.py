class Person:
    count = 0
    def __init__(self,fname,lname,age) -> None:
        Person.count += 1
        self.fname = fname
        self.lname = lname
        self.age = age

p1 = Person("Subham","Nayak",24)
p2 = Person("Subham","Nayak",24)
p3 = Person("Subham","Nayak",24)
print(Person.count)

