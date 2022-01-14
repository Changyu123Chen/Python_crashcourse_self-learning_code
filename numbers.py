#在Python中，可对整数执行加(+ )减(- )乘(* )除(/ )运算。
print(2 + 3)
print(2 - 3)
print(2 * 3)
print(2 / 3)

#乘方运算
print(3 ** 2)
print(2 ** 3)
print((3 ** 2) > (2 ** 3))

#次运算
print(2 + 3*4)
'''
空格不影响Python计算表达式的方式，它们的存在旨在 让你阅读代码时，能迅速确定先执行哪些运算。
'''
#取余&整除
print(3//2)
print(3%2)
#浮点数。结果包含的小数位数可能是不确定的。
print(0.2+0.1)
print(0.2+0.2)
print(0.1+0.1)
print(2*0.3)
print(3*0.1)
print(4*0.1)
print(7*0.1)

'''
所有语言都存在这种问题，没有什么可担心的。
Python会尽力找到一种 方式，以尽可能精确地表示结果，
但鉴于计算机内部表示数字的方 式，这在有些情况下很难。
就现在而言，暂时忽略多余的小数位数即可
'''

#使用函数str() 避免类型错误
age = 23
message = "Happy" + " " + str(age) + "rd Birthday!"
print(message)
'''
age = 23
message = "Happy" + " " + age + "rd Birthday!"
print(message)
会报错。因为age是一个整数（int）的变量。不同的类型无法相加减。需要通过类型的转换。
此处用str（）将int转化为字符串
'''