## testing oop

class Dog:
    def __init__(self, name, price):
        self.name = name
        self.price = float(price)

smalldog = Dog("little",5.40)
meduimdog = Dog("mbat",10.00)

print(smalldog.name)
print(meduimdog.price)
