'''
7-4 比萨配料 :编写一个循环，提示用户输入一系列的比萨配料， 并在用户输入'quit' 时结束循环。
每当用户输入一种配料后，都 打印一条消息，说我们会在比萨中添加这种配料。
'''
message = "配什么料？"
message += "(选好了输入quit)"
a = ' '
while a != "quit":
    a = input(message)
    print("我们会在pizza中加" + a)
'''
7-5 电影票 :有家电影院根据观众的年龄收取不同的票价:不到3 岁的观众免费;3~12岁的观众为10美元;
超过12岁的观众为15美 元。请编写一个循环，在其中询问用户的年龄，并指出其票价。
'''
age = input("您的年龄是：")
age = int(age)
if age<3:
    print("free")
elif age<12:
    print("Your ticket price is $10.")
else:
    print("Your ticket price is $15.")
'''
7-6 三个出又 :以另一种方式完成练习7-4或练习7-5，在程序中采 取如下所有做法。
在while 循环中使用条件测试来结束循环。 使用变量active 来控制循环结束的时机。
使用break 语句在用户输入'quit' 时退出循环。
'''
message = "配什么料？"
message += "(选好了输入quit)"
a = ' '
while a != "quit":
    a = input(message)
    if a != 'quit':
        print("我们会在pizza中加" + a)
'''
7-7 无限循环 :编写一个没完没了的循环，并运行它(要结束该循 环，可按Ctrl +C，也可关闭显示输出
的窗又)。
'''
pizza = input("Enter what topping you want.(You can enter quit after finishing selecting.)")
while True:
    if pizza != 'quit':
        print("We will add " + pizza + "in your pizza")
