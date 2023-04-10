#e-comerce system :
#Aji Raida
#Rafi


class product:
  def __init__(self, name, price, quantity):
    self.name = str(name)
    self.price = float(price)
    self.quantity = int(quantity)
    
  def get_name(self):
        return self.name
    
  def get_price(self):
        return self.price
    
  def get_quantity(self):
        return self.quantity
      
  def update_quantity(self, quantity):
        self.quantity += quantity
    
class Electronics(product):
   def __init__(self, name, price, quantity, warranty_period):
       super().__init__(name, price, quantity)
       self.warranty_period = str(warranty_period)
       
   def get_warranty_period(self):
        return self.warranty_period
    
class Clothing(product):
     def __init__(self, name, price, quantity, size):
         super().__init__(name, price, quantity)
         self.size = str(size)
         
     def get_size(self):
       return self.size
    
class Book(product):
     def __init__(self, name, price, quantity, author):
         super().__init__(name, price, quantity)
         self.author = str(author)
         
     def get_author(self):
         return self.author

class chart:
  
  def __init__(self):
        self.items = []
      
  def add_items(self, data):
      sama = False
      for i in range(len(self.items)):
            if self.items[i]['name'] == data['name']:
                sama = True
                
      if sama == True:
          self.items[i]['quantity'] += 1
      else:
          self.items.append(data)
      print(f"Product Added To Cart: {data['name']}")
      print()
   
  def remove_items(self, rmv):
        product5 = {}
        product5['name'] = self.items[int(rmv) - 1]['name']
        product5['quantity'] = self.items[int(rmv) - 1]['quantity']
        print("========================")
        print(f"{self.items[int(rmv) - 1]['name']} Delete successfully")
        print("========================")
        self.items.pop(int(rmv) - 1)
        return product5
    
  def view_items(self):
        j = 0
        for i in self.items:
            j += 1
            print(f"{j}. {i['name']}, Rp.{i['price']} - {i['quantity']} pcs")

  def place_order(self):
     total_price = 0
     for i in self.items:
        total_price += (i['price'] * i['quantity'])    
     print("Total Price : ", total_price)
     print("Thank you for shoping with us!!")

product1 = Electronics('Realme GT', 150000000, 50, "1 year")
product2 = Electronics('Asus TravelMate', 2000000,  50, "2 Year")
product3 = Clothing('Takahiro', 750000, 90, "L")
product4 = Book('The Chronicles Of Narnia', 25000, 100, "C.S Lewis")

cart = chart()