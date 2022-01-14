'''
5-8 以特殊方式跟管理员打招呼 :创建一个至少包含5个用户名的 列表，
且其中一个用户名为'admin' 。想象你要编写代码，在每 位用户登录网站后都打印一条问候消息。
遍历用户名列表，并向 每位用户打印一条问候消息。
如果用户名为'admin' ，就打印一条特殊的问候消息， 
如“Hello admin, would you like to see a status report?”。
否则，打印一条普通的问候消息，如“Hello Eric, thank you for logging in again”。
'''
'''
5-9 处理没有用户的情形 :在为完成练习5-8编写的程序中，添加 一条if 语句，
检查用户名列表是否为空。
如果为空，就打印消息“We need to find some users!”。
删除列表中的所有用户名，确定将打印正确的消息。
'''
users = ['admin', 'Alice', 'Kitty', 'Ben', 'Tom']
if users:
	for user in users:
		print("Hello, " + user + " thank you for logging in again!")
else:
	print("We need to find some users!")


'''
5-10 检查用户名 :按下面的说明编写一个程序，模拟网站确保每 位用户的用户名都独一无二的方式。
创建一个至少包含5个用户名的列表，并将其命名为 current_users 。
再创建一个包含5个用户名的列表，将其命名为new_users ，
并确保其中有一两个用户名也包含在列表current_users 中。
遍历列表new_users ，对于其中的每个用户名，都检查它是 否已被使用。
如果是这样，就打印一条消息，指出需要输入 别的用户名;否则，打印一条消息，
指出这个用户名未被使 用。
确保比较时不区分大消息;换句话说，如果用户名'John' 已 被使用，应拒绝用户名'JOHN' 。
'''
current_users = ['Peter', 'Alice', 'Kitty', 'Ben', 'Tom']
new_users = ['peter', 'Kitty', 'zhangsan', 'lisi','wangerma']
current_users = [current_user.lower() for current_user in current_users]
new_users = [new_user.lower() for new_user in new_users]
for new_user in new_users:
	if new_user in current_users:
		print("This name has been used. Please input other username")
	else:
		print("This name have not been used")
'''
5-11 序数 :序数表示位置，如1st和2nd。大多数序数都以th结尾， 只有1、2和3例外。
在一个列表中存储数字1~9。
遍历这个列表。
在循环中使用一个if-elif-else 结构，以打印每个数字对 应的序数。
输出内容应为1st 、2nd 、3rd 、4th 、5th 、 6th 、7th 、8th 和9th ，
但每个序数都独占一行。
'''
numbers = list(range(1,10))
for number in numbers:
	if number == 1:
		print("1st")
	elif number == 2:
		print("2nd")
	elif number == 3:
		print("3rd")
	else:
		print(str(number) + "th")