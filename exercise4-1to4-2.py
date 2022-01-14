'''
4-1 比萨 :想出至少三种你喜欢的比萨，将其名称存储在一个列表中，
再使用for 循环将每种比萨的名称都打印出来。

修改这个for 循环，使其打印包含比萨名称的句子，而不仅 仅是比萨的名称。
对于每种比萨，都显示一行输出，如“I like pepperoni pizza”。

在程序末尾添加一行代码，它不在for 循环中，指出你有多 喜欢比萨。输出应包含针对每种比萨的消息，
还有一个总结 性句子，如“I really love pizza!”。
'''
pizzas = ["beef pizza", "pork pizza", "sausages pizza"]
for pizza in pizzas:
	print("I like " + pizza)
print("I really love pizza!")
'''
4-2 动物 :想出至少三种有共同特征的动物，将这些动物的名称存 储在一个列表中，
再使用for 循环将每种动物的名称都打印出 来。

修改这个程序，使其针对每种动物都打印一个句子，如“A dog would make a great pet”。

在程序末尾添加一行代码，指出这些动物的共同之处，如打 印诸如“Any of these animals would make a great pet!”这样的句 子。
'''
animals = ['dog', 'cat', 'mouse']
for animal in animals:
	print('A ' + animal + " would make a great pet!")
print('Any of these animals would makes a great pet!')