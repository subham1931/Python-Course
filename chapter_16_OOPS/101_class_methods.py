class Person:
    count = 0 #class variabel/attruibute
    def __init__(self,fname,lname,age) -> None:
        Person.count += 1
        self.fname = fname
        self.lname = lname
        self.age = age

    @classmethod
    def count_instance(cls):
        return f"You have created {cls.count} instances of Person"

p1 = Person("Subham","Nayak",24)
p2 = Person("Subham","Nayak",24)
p3 = Person("Subham","Nayak",24)
print(Person.count_instance())

