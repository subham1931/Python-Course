class Phone:
    def __init__(self,brand,model,price) -> None:
        self.brand = brand
        self.model = model
        self.__price = price
        self.all = f"{brand} {model} {price}"

    def makeCall(self,mob):
        print(f"Calling {mob}")

    def fullName(self):
        return f'{self.brand} {self.model}'


class SmartPhone(Phone):
    def __init__(self, brand, model, price,ram,rom) -> None:
        super().__init__(brand, model, price)
        self.ram = ram
        self.rom = rom

sp = SmartPhone('Apple','11','50000','8','128')
print(sp.fullName())