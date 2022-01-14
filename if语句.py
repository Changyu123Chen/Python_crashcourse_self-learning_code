fruits = ["cherry", "orange", "apple"]
for fruit in fruits:
	if fruit == "cherry":
		print(fruit.upper())
	else:
		print(fruit.title())

if 18>19:
	print(True)
else:
	print("18<19")

if 18<19:
	print(True)

if 18==19:
	print(True)
else:
	print(False)

if (18>16) and (15<16):
	print(True)

if(18>19) or (16>15):
	print(True)
else:
	print(False)

if "cherry" in fruits:
	print(fruits)
if "Mango" not in fruits:
	print(fruits)

#5.3 if 语句
age = 19
if age >= 18:
	print("You are old enough to vote!")
	print("Have you registered to vote yet?")

#5.3.2 if-else语句
ages = [12, 15, 18, 10, 20, 80]
for age in ages:
	if age >= 18:
		print("Your age is " + str(age))
		print("You are old enough to vote!")
		print("Have you registered to vote yet?")	
	else:
		print("Your age is " + str(age)) 
		#注意age是整数型，不可与str相加。需要先转换类型
		#print("Your age is " + age)会报错
		print("Sorry, you are too young to vote.")
		print("Please register to vote as soon as you turn 18!")

#5.3.3 if-elif-else结构/5.3.4 使用多个elif 代码块/5.3.5 省略else 代码块
'''
if-elif-else 结构功能强大，但仅适合用于只有一个条件满足的情 况:
遇到通过了的测试后，Python就跳过余下的测试。这种行为很好， 效率很高，
让你能够测试一个特定的条件。
'''
nianling = [2, 3, 6, 19, 10, 30, 80, 18]
for a in nianling:
	if a <= 10:
		print("Your age is " + str(a))
		print("Your ticket price is $0.")
	elif a<=20:
		print("Your age is " + str(a))
		print("Your ticket price is $5.")
	elif a>=80:
		print("Your age is " + str(a))
		print("Your ticket price is $0.")
	else:
		print("Your age is " + str(a))
		print("Your ticket price is $30.")
	#elif a<80:
		#print("Your age is " + str(a))
		#print("Your ticket price is $30.")




'''
应使用一 系列不包含elif 和else 代码块的简单if 语句。
在可能有多个条件为 True ，且你需要在每个条件为True 时都采取相应措施时，适合使用 这种方法。
'''
##5.4 使用if 语句处理列表
requested_toppings = ['mushroom', 'extra cheese']
if 'mushroom' in requested_toppings:
	print("Adding mushrooms.")
if 'extra cheese' not in requested_toppings:
	print("1")
else:
	print("Adding extra cheese.")

print("\nFinished making your pizza!")
'''
总之，如果你只想执行一个代码块，就使用if-elif-else 结构;
如 果要运行多个代码块，就使用一系列独立的if 语句。
'''

#5.4.2 确定列表不是空的
requested_toppings = [ ]
if requested_toppings:
	for requested_topping in requested_toppings:
		print("Adding" + requested_topping)
		print("\nFinished making or pizza")
else:
	print("Are you sure you want a plan pizza?")



#5.4.3 使用多个列表
available_toppings = ['mushroom', 'onion', 'tomato','cheese']
requested_toppings = ['cheese', 'potato']
for requested_topping in requested_toppings:
	if requested_topping in available_toppings:
		print("Adding " + requested_topping)
	else:
		print("We don't have " + requested_topping)