class Phone:
    def __init__(self,brand,model,price) -> None:
        self.brand = brand
        self.model = model
        self.__price = price

    def makeCall(self,mob):
        print(f"Calling {mob}")

    def fullName(self):
        print(f'{self.brand} {self.model}')


p1 = Phone('Apple','11',50000)
print(p1.__dict__)