class Car():
    def __init__(self, make, model, year):
        '''
        定义了一个self
        (其实定义什么都可以，只要后面保证被定义的这个参数所包含的内容传输到后面的def里就行了)
        make, model, year: 方法__init__() 接受这些形参的值， 并将它们存储在根据这个类创建的实
        例的属性中
        '''
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name.title()
    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")
    def update_odometer(self, mileage):#2. 通过方法修改属性的值
        self.odometer_reading = mileage
    def increment_odometer(self, miles):#3. 通过方法对属性的值进行递增
        self.odometer_reading += miles
my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(23)
my_new_car.increment_odometer(100)
my_new_car.read_odometer()

class ElectricCar(Car):#父类必须包含在当前文件 中，且位于子类前面
    def __init__(self, make, model, year):
        super().__init__(make,model,year)
#处的super() 是一个特殊函数，帮助Python将父类和子类关联起来。
        #父类也称为超类 (superclass)，名称super因此而得名
        self.battery_size = 70
    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kWh battery.")
my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
