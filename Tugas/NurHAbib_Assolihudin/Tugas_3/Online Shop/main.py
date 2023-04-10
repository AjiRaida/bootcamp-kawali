# MAIN PAGE
from Product import fuji_film, sharp, gucci, atomic_habit, detektif_conan_v1
from Chart import chart

def main():
    data = {}
    print("=== WELCOME TO OUR ONLINE SHOP SYSTEM ===")
    print("-----------------------------------------")
    print()
    print("Available Product : ")
    print("====================")
    print(f"1. {fuji_film.name} (Electronics) - Price Rp.{fuji_film.price}, Quantity:{fuji_film.quantity} -- Warranty Period Is {fuji_film.warranty_period} month")
    print(f"2. {sharp.name} (Electronics) - Price Rp.{sharp.price}, Quantity:{sharp.quantity} -- Warranty Period Is {sharp.warranty_period} month")
    print(f"3. {gucci.name} (Clothing) - Price Rp.{gucci.price}, Quantity:{gucci.quantity} -- Size Is {gucci.size}")
    print(f"4. {atomic_habit.name} (Book) - Price Rp.{atomic_habit.price}, Quantity:{atomic_habit.quantity} -- Author Is {atomic_habit.author}")
    print(f"5. {detektif_conan_v1.name} (Book) - Price Rp.{detektif_conan_v1.price}, Quantity:{detektif_conan_v1.quantity} -- Author Is {detektif_conan_v1.author}")
    print()
    choise = input("Input the number for add product to chart (or 0 for exit to chart): ")
    print()
    if choise == "1":
        data.update({
            "name" : fuji_film.getName(),
            "price" : fuji_film.getPrice(),
            "quantity" : 1
        })
        chart.addToChart(data)
        fuji_film.updateQuantity(-1)
    elif choise == "2":
        data.update({
            "name": sharp.getName(),
            "price": sharp.getPrice(),
            "quantity": 1
        })
        chart.addToChart(data)
        sharp.updateQuantity(-1)
    elif choise == "3":
        data.update({
            "name": gucci.getName(),
            "price": gucci.getPrice(),
            "quantity": 1
        })
        chart.addToChart(data)
        gucci.updateQuantity(-1)
    elif choise == "4":
        data.update({
            "name": atomic_habit.getName(),
            "price": atomic_habit.getPrice(),
            "quantity": 1
        })
        chart.addToChart(data)
        atomic_habit.updateQuantity(-1)
    elif choise == "5":
        data.update({
            "name": detektif_conan_v1.getName(),
            "price": detektif_conan_v1.getPrice(),
            "quantity": 1
        })
        chart.addToChart(data)
        detektif_conan_v1.updateQuantity(-1)
    elif choise == "0":
        return False
    else:
        print("Not Validated Input")

def chartS():
    print("=== CHART ===")
    print("-------------")
    chart.viewChart()
    print()
    choice = input("Enter 1 to place order, 2 to remove product, or 0 to exit : ")
    if choice == "1":
        chart.placeOrder()
    elif choice == "2":
        product = input("Enter the number of product : ")
        product2 = chart.removeFromChart(product)
        if product2['name'] == "Fuji Film":
            fuji_film.updateQuantity(product2['quantity'])
        elif product2['name'] == "Sharp":
            sharp.updateQuantity(product2['quantity'])
        elif product2['name'] == "Gucci":
            gucci.updateQuantity(product2['quantity'])
        elif product2['name'] == "Atomic Habit":
            atomic_habit.updateQuantity(product2['quantity'])
        elif product2['name'] == "Detektif Conan Vol.1":
            detektif_conan_v1.updateQuantity(product2['quantity'])
    elif choice == "0":
        return False
    else:
        print("Not Validated Input")


while True:
    kondisi = main()
    if kondisi == False:
        break
while True:
    kondisi = chartS()
    if kondisi == False:
        break