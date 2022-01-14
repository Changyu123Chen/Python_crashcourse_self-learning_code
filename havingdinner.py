'''
9-4 就餐人数 :在为完成练习9-1而编写的程序中，添加一个名为 number_served 的属性，
并将其默认值设置为0。根据这个类创 建一个名为restaurant 的实例;打印有多少人在这家餐馆就餐
过，然后修改这个值并再次打印它。
添加一个名为set_number_served() 的方法，它让你能够设置 就餐人数。调用这个方法并向它传递一个值，然后再次打印这个 值。
添加一个名为increment_number_served() 的方法，它让你 能够将就餐人数递增。调用这个方法并向它传
一个这样的值: 你认为这家餐馆每天可能接待的就餐人数。
'''

'''
9-1 餐馆 :创建一个名为Restaurant 的类，其方法 __init__() 设置两个属性:restaurant_name
和 cuisine_type 。创建一个名为describe_restaurant() 的 方法和一个名为open_restaurant()
的方法，其中前者打印前 述两项信息，而后者打印一条消息，指出餐馆正在营业。
'''
class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    def describe_restaurant(self):
        print(self.restaurant_name + " " + self.cuisine_type)

    def open_restaurant(self):
        print("The restaurant is now open.")

    def set_number_served(self, number):
        self.number_served = number
        print(self.number_served)
    def increment_number_served(self,number1):
        self.number_served += number1
        print(self.number_served)
        
people = Restaurant('KFC','Chicken Wings')
people.describe_restaurant()
people.open_restaurant()
people.set_number_served(20)
people.increment_number_served(100)
