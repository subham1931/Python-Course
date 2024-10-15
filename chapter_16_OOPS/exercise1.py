class Laptop:
    def __init__(self,brand,model,price) -> None:
        self.brand = brand
        self.model = model
        self.price = price
        self.laptopname = brand + " " + model

l1 = Laptop('ASUS',"TUF",'100000')
l2 = Laptop('ASUS',"ROG",'120000')

print(l1.laptopname)
print(l2.laptopname)