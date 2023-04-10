# CLASS PRODUCT
# Class Electronics (Child OF Product CLass)
# Class Clothing (Child OF Product CLass)
# Class Book (Child OF Product CLass)

# Class
class Product:
    def __init__(self, name, price, quantity):
        self.name = str(name)
        self.price = float(price)
        self.quantity = int(quantity)

    def getName(self):
        return self.name

    def getPrice(self):
        return self.price

    def getQuantity(self):
        return self.quantity

    def updateQuantity(self, quantity):
        self.quantity += quantity


class Electronics(Product):
    def __init__(self, name, price, quantity, warranty_period):
        super().__init__(name, price, quantity)
        self.warranty_period = int(warranty_period)

    def getWarrantyPeriod(self):
        return self.warranty_period

class Clothing(Product):
    def __init__(self, name, price, quantity, size):
        super().__init__(name, price, quantity)
        self.size = str(size)

    def getSize(self):
        return self.size

class Book(Product):
    def __init__(self, name, price, quantity, author):
        super().__init__(name, price, quantity)
        self.author = str(author)

    def getAuthor(self):
        return self.author

# Object
fuji_film = Electronics("Fuji Film", 10000000, 50, 5)
sharp = Electronics("Sharp", 5000000, 15, 3)
gucci = Clothing("Gucci", 2000000, 60, "L")
atomic_habit = Book("Atomic Habit", 25000, 18, "James Clear")
detektif_conan_v1 = Book("Detektif Conan Vol.1", 35000, 12, "NurHabib")