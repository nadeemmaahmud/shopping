class Shop():
    def __init__(self, name) -> None:
        self.name = name
        self.cart = []

    def addToCart(self, item, price, quantity):
        self.item = item
        self.price = price
        self.quantity = quantity

        self.cart.append({'item' : item, 'price' : price, 'quantity' : quantity})

    def checkOut(self):
        self.price = 0

        for i in self.cart:
            self.price += i['price'] * i['quantity']
        
        print("Your total bill is : ", self.price)

    def payment(self, amount):
        if amount > self.price:
            print("Hey", self.name, ", Shopping done! Here is you extra amount :", amount - self.price)
        elif amount < self.price:
            print("Hey", self.name, "!, kindly pay more :", self.price - amount)
        else:
            print("Thanks for shopping with us", self.name, "!")

myShop = Shop(input("Enter you name : "))

myShop.addToCart('Alu', 20, 2)
myShop.addToCart('Begun', 25, 1)
myShop.addToCart('Piaj', 110, .5)

myShop.checkOut()

myShop.payment(int(input("Enter your amount : ")))