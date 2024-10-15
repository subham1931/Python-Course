#Class variable
class Circle:
    ##Class variable
    pi = 3.14
    def __init__(self,radius) -> None:
        self.radius = radius

    def calc_circle(self):
        return 2*Circle.pi*self.radius
    

c1 = Circle(4)
c2 = Circle(5)
print(c1.calc_circle())
print(c1.__dict__)