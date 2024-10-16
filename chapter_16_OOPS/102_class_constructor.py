class Person:
    count = 0 #class variabel/attruibute
    def __init__(self,fname,lname,age) -> None:
        Person.count += 1
        self.fname = fname
        self.lname = lname
        self.age = age

##constructor
    @classmethod
    def fromString(cls,string):
        f,l,a=string.split(',')
        return cls(f,l,a)

    @classmethod
    def count_instance(cls):
        return f"You have created {cls.count} instances of Person"
    
    @staticmethod
    def pr():
        print("Static methos calling")

p1 = Person("Subham","Nayak",24)
p2 = Person("Subham","Nayak",24)
p3 = Person.fromString("Subham,Nayak,24")
print(p3.fname)
Person.pr()##Static methos calling
print(Person.count_instance())

