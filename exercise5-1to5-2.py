fruits = ['cherry', 'mango', 'apple', 'grape', 'peach']
'''
5-1 条件测试 :编写一系列条件测试;将每个测试以及你对其结果 
的预测和实际结果都打印出来。你编写的代码应类似于下面这 样:
'''
fruit = "Mango"
print("Is fruit == 'Mango'? I predit True.")
print(fruit == "Mango")
print("Is fruit =='cherry'? I predit False.")
print(fruit =="cherry")

'''
5-2 更多的条件测试 :你并非只能创建10个测试。如果你想尝试做更多的比较，
可再编写一些测试，并将它们加入到conditional_tests.py中。对于下面列出的各种测试，
至少编写一个 结果为True 和False 的测试。
'''
#检查两个字符串相等和不等。
print("abc"=="ABC")
print("abc"=="abc")
#使用函数lower() 的测试。
print("abc"=="ABC".lower())
#检查两个数字相等、不等、大于、小于、大于等于和小于等于。
print(1>2)
print(1<2)
print(1==2)
print(1>=2)
print(1<=2)
#使用关键字and 和or 的测试。
print(1>0 and 1<2)
print(1>2 and 1<2)
print(1<2 or 1>2)
print(1<2 or 1<2)
print(1==2 or 1<2)
#测试特定的值是否包含在列表中。/测试特定的值是否未包含在列表中。
print("mango" in fruits)
print("pear" not in fruits)
print("cherry" in fruits)
