class Person:
    def __init__(self,fname,lname,age) -> None:
        self.fname = fname
        self.lname = lname
        self.age = age

    def fullName(self):
        return f"{self.fname} {self.lname}"
    
    def elegibe(self):
       return self.age >= 18

p1 = Person("Subham","Nayak",24)

print(p1.fullName())
print(p1.elegibe())


# l = [1,2,3,4,5]


# l.clear()
# list.clear(l)


# list.append(l,10)
# l.append(10)
# print(l)