class Laptop:
    def __init__(self,brand,model,price) -> None:
        self.brand = brand
        self.model = model
        self.price = int(price)
        self.laptopname = brand + " " + model

    def discount(self):
        discountPrice = (20/100) * self.price
        return self.price - discountPrice

l1 = Laptop('ASUS',"TUF",'100000')
l2 = Laptop('ASUS',"ROG",'120000')

print(l1.laptopname,l1.discount())
print(l2.laptopname,l2.discount())