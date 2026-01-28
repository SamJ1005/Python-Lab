class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display_product(self):
        print("Product Name:", self.name)
        print("Price: ₹", self.price)


class ElectronicsProduct(Product):
    def __init__(self, name, price, brand, warranty):
        super().__init__(name, price)
        self.brand = brand
        self.warranty = warranty

    def display_electronics(self):
        self.display_product()
        print("Brand:", self.brand)
        print("Warranty:", self.warranty, "years")

name = input("Enter product name: ")
price = float(input("Enter price: "))
brand = input("Enter brand: ")
warranty = int(input("Enter warranty period (years): "))

e = ElectronicsProduct(name, price, brand, warranty)
print("\nElectronic Product Details:")
e.display_electronics()
