nums = [1,2,3,4,5,6,7,9,10, 1,2,3,4,5,6,7]
letters = ['a','b','c','d','e','f','h']
words = ['I', 'forget', 'everything', 'about', 'python', 'after', 'learning', 'C']

print("********列表中的最大值********")
print(max(nums))
print(max(letters))
print(max(words))

print("********列表中的最小值********")
print(min(nums))
print(min(letters))
print(min(words))

print("********出现次数********")
print(nums.count(1))#one item a time
print(letters.count('a'))
print(words.count('forget'))

print("********移除********")
print(nums.remove(1))
print(nums)
letters.remove('a')
print(letters)
words.remove('forget')
print(words)

print("********添加********")
index = 0
nums.insert(index, 1)
print(nums)
letters.insert(index, 'a')
print(letters)
words.insert(1, 'forget')
print(words)

print("********列表倒转********")
nums.reverse()
print(nums)
letters.reverse()
print(letters)
words.reverse()
print(words)

print("*******添加元素********")
nums.append(8)
print(nums)
letters.append('s')
print(letters)
words.append('才怪')
print(words)

print("*******寻找元素第一次出现的位置********")
print(nums.index(3))
print(letters.index('s'))
print(words.index('python'))


print()
print()
print()
print()
print(" ********************************************** ")
def Iloveyou():
    print("fake")

Iloveyou()
print("************************************************* ")
print("Returing from Functions")
def add_numbers(x, y):
    total = x + y
    return total
    print('This won\'t be printed')
add_numbers(4, 5)
print("lalallallalla")
print(add_numbers(4, 5))


print("************************************************* ")
def Abab(x, y):

    if (x<=y) :

        return x
    else:
        return y
    print(x, y)
Abab(1, 2)
print(Abab(1, 2))
print("************************************************* ")
def abab_1(x):
    res = 0
    for i in range(x):
        res += i;
    return res
abab_1(4)
print(abab_1(4))
print("************************************************* ")
print("************************************************* ")
def search():
    a = input()
    b = input()
    if (a.count(b) != 0):
        print('Word found')
    else:
        print('Word not found')
search()

