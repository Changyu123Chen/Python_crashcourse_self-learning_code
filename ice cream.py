class restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self): #记得加self
        print(self.restaurant_name.upper())
        print(self.cuisine_type.title())
    def open_restaurant(self):
        print("The restaurant is open")

class IceCreamStand(restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []

    def icecream_flavors(self, *flavor):
        self.flavors.append(flavor)
        print(self.flavors)
icecream = IceCreamStand('暴风雪','冰淇淋')
icecream.describe_restaurant()
icecream.icecream_flavors('1','2')
