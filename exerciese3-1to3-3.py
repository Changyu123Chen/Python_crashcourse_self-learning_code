'''
3-1 姓名: 将一些朋友的姓名存储在一个列表中，并将其命名为 names 。
依次访问该列表中的每个元素，从而将每个朋友的姓名 都打印出来。
'''
names = ["张三", "李四", "王二麻"]
for name in names:
	print(name)

'''
3-2 问候语: 继续使用练习3-1中的列表，但不打印每个朋友的姓名，而为每人打印一条消息。
每条消息都包含相同的问候语，但 抬头为相应朋友的姓名。
'''
for name in names:
	print(name + '你好')


'''
3-3 自己的列表: 想想你喜欢的通勤方式，如骑摩托车或开汽车， 并创建一个包含多种通勤方式的列表。
据该列表打印一系列有 关这些通勤方式的宣言，如“I would like to own a Honda motorcycle”。
'''
vehicles = ["bicycle","motorcycle","car","helicopter","ship"]
for vehicle in vehicles:
	print("I would like to own a " + vehicle)