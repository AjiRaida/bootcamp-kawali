# CLASS CHART

class Chart:
    def __init__(self):
        self.items = []

    def addToChart(self, data):
        sama = False
        for i in range(len(self.items)):
            if self.items[i]['name'] == data['name']:
                sama = True

        if sama == True:
            self.items[i]['quantity'] += 1
        else:
            self.items.append(data)
        print(f"{data['name']} is added")
        print()

    def removeFromChart(self, product):
        product2 = {}
        product2['name'] = self.items[int(product) - 1]['name']
        product2['quantity'] = self.items[int(product) - 1]['quantity']
        print(f"{self.items[int(product) - 1]['name']} has deleted")
        self.items.pop(int(product) - 1)
        return product2

    def viewChart(self):
        j = 0
        for i in self.items:
            j += 1
            print(f"{j}. {i['name']}, Rp.{i['price']} - {i['quantity']} buah")

    def placeOrder(self):
        total_price = 0
        for i in self.items:
            total_price += (i['price'] * i['quantity'])
        print(f"Total Price : {total_price}")
        print("Thank you for shoping with us!!")

chart = Chart()