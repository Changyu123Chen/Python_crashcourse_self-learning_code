#索引从0开始而不是1
fruits = ["apple", "orange", "mango", "peach", "cherry"]
print(fruits[3].title())
'''
Python为访问最后一个列表元素提供了一种特殊语法。
通过将索引指定 为-1 ，可让Python返回最后一个列表元素这种语法很有用，
因为你经常需要 在不知道列表长度的情况下访问最后的元素。
'''
print(fruits[-2].title())
#在方括号内先做数的运算，再输出列表中的对象
print(fruits[3-2].title()) #输出orange
print(fruits[2-3].title())#cherry


#使用列表中的各个值
message = "My favourite fruit are " + fruits[3] + "es."
print(message)
