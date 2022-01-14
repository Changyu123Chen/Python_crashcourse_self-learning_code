'''
6-7 人 :在为完成练习6-1而编写的程序中，再创建两个表示人的字典，
然后将这三个字典都存储在一个名为people 的列表中。
遍历这个列表，将其中每个人的所有信息都打印出来。
'''
zhang = {
	'first_name': '三',
	'last_name':'张', 
	'gender':'male', 
	'age': 19, 
	'residence': 'Shanghai'
}
li = {
	'first_name': '四',
	'last_name':'李', 
	'gender':'male', 
	'age': 25, 
	'residence': 'Beijing'
}
wang = {
	'first_name': '二麻',
	'last_name':'王', 
	'gender':'male', 
	'age': 30, 
	'residence': 'Shandon'
}
peoples = [zhang, li, wang]
for people in peoples:
	for element in people.items():
		full_name = people['last_name']+people['first_name']
		gender = people['gender']
		age = people['age']
		residence = people['residence']
	print("fullname: " + full_name)
	print("gender: " + gender)
	print("age: " + str(age))
	print('residence: ' + residence)

'''
6-8 宠物 :创建多个字典，对于每个字典，都使用一个宠物的名称 
来给它命名;在每个字典中，包含宠物的类型及其主人的名字。 
将这些字典存储在一个名为pets 的列表中，再遍历该列表，
并将宠物的所有信息都打印出来。
'''
lala = {
	'name': 'lala',
	'type': 'dog',
	'gender': 'male',
	'owner':'a',
}
soso = {
	'name': 'soso',
	'type': 'cat',
	'gender': 'female',
	'owner':'b',
}
dodo = {
	'name': 'dodo',
	'type': 'dog',
	'gender': 'female',
	'owner':'c',
}
pets = [lala, soso, dodo]
for pet in pets:
	for keys, values in pet.items():
		print(keys + ": " + "\n" + values)

'''
6-9 喜欢的地方 :创建一个名为favorite_places 的字典。在 这个字典中，
将三个人的名字用作键;对于其中的每个人，都存 储他喜欢的1~3个地方。
为让这个练习更有趣些，可让一些朋友指 出他们喜欢的几个地方。
遍历这个字典，并将其中每个人的名字 及其喜欢的地方打印出来。
'''
favorite_places = {
	'Alice': {
	"first": "shandon",
	"second": "hubei",
	"third":"neimeng",
	},
	'Kitty': {
	"first" :"shanghai",
	"second":'dezhou',
	"third":'xianggang'
	},
	'Ben': {"first": "Beijing"},
}
for key, values in favorite_places.items():
	print(key + ':')
	for key_1, element in values.items():
		print(key_1 + ": " + element)
'''
6-10 喜欢的数字 :修改为完成练习6-2而编写的程序，
让每个人都 可以有多个喜欢的数字，然后将每个人的名字及其喜欢的数字打 
印出来。
'''
favorite_numbers = {
	'Alice':{1: 1, 2: 4, 3: 5, 4: 18},
	'Kitty':{1:2, 2:34, 3:3, 4: 5, 5:18, 6:20, 7:45},
	'Ben':{1:35, 2:45},
}
for key, values in favorite_numbers.items():
	print(key + ':')
	for key_1, element in values.items():
		print(str(key_1) + ": " + str(element))


'''
6-11 城市 :创建一个名为cities 的字典，其中将三个城市名用 作键;
对于每座城市，都创建一个字典，并在其中包含该城市所
属的国家、人又约数以及一个有关该城市的事实。在表示每座城 市的字典中，
应包含country 、population 和fact 等键。将 每座城市的名字以及有关它们
的信息都打印出来。
'''
#我好累 不写了