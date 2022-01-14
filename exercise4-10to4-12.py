'''
4-10 切片 :选择你在本章编写的一个程序，在末尾添加几行代 码，以完成如下任务。
打印消息“The first three items in the list are:”，再使用切片来打 印列表的前三个元素。
打印消息“Three items from the middle of the list are:”，再使用 切片来打印列表中间的三个元素。
打印消息“The last three items in the list are:”，再使用切片来打 印列表末尾的三个元素。
'''
integers = list(range(1, 11))
print("The first three items in the list are:")
print(integers[1:4])
print("Three items from the middle of the list are:")
print(integers[3: 6])
print("The last three items in the list are:")
print(integers[-3:])

'''
4-11 你的比萨和我的比萨 :在你为完成练习4-1而编写的程序中， 
创建比萨列表的副本，并将其存储到变量friend_pizzas 中， 再完成如下任务。
在原来的比萨列表中添加一种比萨。 在列表friend_pizzas 中添加另一种比萨。
核实你有两个不同的列表。为此，打印消息“My favorite pizzas are:”，
再使用一个for 循环来打印第一个列表;打印消 息“My friend's favorite pizzas are:”，
再使用一个for 循环来打 印第二个列表。核实新增的比萨被添加到了正确的列表中。
'''
my_favourite_pizzas = ["mushroom pizza", "beef pizza", "pork pizza"]
friend_pizzas = my_favourite_pizzas[:]
my_favourite_pizzas.append("fruit pizza")
friend_pizzas.append("fish pizza")
for my_favourite_pizza in my_favourite_pizzas:
	print(my_favourite_pizza)
for friend_pizza in friend_pizzas:
	print(friend_pizza)
print(my_favourite_pizzas)
print(friend_pizzas)

'''
4-12 使用多个循环 :在本节中，为节省篇幅，
程序foods.py的每个版本都没有使用for 循环来打印列表。
请选择一个版本的foods.py，在其中编写两个for 循环，将各个食品列表都打印出来。
'''
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)
for my_food in my_foods:
	print(my_food)
for friend_food in friend_foods:
	print(friend_food)




print("*******************************************************")
#元组 其中的元素无法修改
dimension = (20, 50)
print(dimension[1])
#print(dimension[0])
#dimension[0] = 100 报错
print(dimension)

#修改元组变量
dimensions = (40, 100)
print("\n modified dimensions:")
print(dimensions)