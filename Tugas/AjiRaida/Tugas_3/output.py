from e_comerce import product, cart, product1, product2, product3, product4

def main():
    data = {}
    print("welcome to online shop system")
    print("-----------------------------")
    print("Available Product :")
    print()
    print("1. ",product1.get_name(),"(Electronics)", "- price Rp:",product1.get_price(),",","quantity:",product1.get_quantity(),"warranty_period:",product1.get_warranty_period())
    
    print("2. ",product2.get_name(),"(Electronics)", "- price Rp:",product2.get_price(),"quantity:",product2.get_quantity(),"warranty_period:",product1.get_warranty_period())
        
    print("3. ",product3.get_name(),"(Clothing)", "- price Rp:",product3.get_price(),"quantity:",product3.get_quantity(),"size:",product3.get_size())
        
    print("4. ",product4.get_name(),"(Book)", "- price Rp:",product4.get_price(),"quantity:",product4.get_quantity(),"author:",product4.get_author())
    print()
    choise = input("Input The Number For Add Product To Chart (Or [0] For Exit To Chart):")
    
    print()
    if choise == "1":
        data.update({
            "name" : product1.get_name(),
            "price" : product1.get_price(),
            "quantity" : 1
        })
        cart.add_items(data)
        product1.update_quantity(-1)
    elif choise == "2":
        data.update({
            "name": product2.get_name(),
            "price": product2.get_price(),
            "quantity": 1
        })
        cart.add_items(data)
        product2.update_quantity(-1)
    elif choise == "3":
        data.update({
            "name": product3.get_name(),
            "price": product3.get_price(),
            "quantity": 1
        })
        cart.add_items(data)
        product3.update_quantity(-1)
    elif choise == "4":
        data.update({
            "name": product4.get_name(),
            "price": product4.get_price(),
            "quantity": 1
        })
        cart.add_items(data)
        product4.update_quantity(-1)
    elif choise == "0":
        return False
    else:
        print("Failed")

def chart():
    print("Cart contens:")
    cart.view_items()
    print()
    choice = input("Enter [1] To Place Order, [2] To Remove Product, Or To Exit : ")
    if choice == "1":
        cart.place_order()
    elif choice == "2":
        product = input("Enter the number of product : ")
        productB = cart.remove_items(product)
        if productB['name'] == "product1":
            product1.update_quantity(productB['quantity'])
        elif productB['name'] == "product2":
            product2.update_quantity(productB['quantity'])
        elif productB['name'] == "product3":
            product3.update_quantity(productB['quantity'])
        elif productB['name'] == "product4":
            product4.update_quantity(productB['quantity'])
    elif choice == "0":
        return False
    else:
        print("Input Failed")

while True:
    kondisi = main()
    if kondisi == False:
        break
while True:
    kondisi = chart()
    if kondisi == False:
        break