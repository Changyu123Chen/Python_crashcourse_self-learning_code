with open('/Users/chenchangyu/Desktop/大学准备/Programming/Python/text_files/pi_digits.txt') as file_object:
    lines = file_object.readlines()
    filename = 'text_files/pi_digits.txt'
    contents = file_object.read()
    print(contents)
#要保存到一个文件夹里面 才可以访问
    print(contents.rstrip())
    ##10.1.3 逐行读取
    for line in file_object:
        print(line.rstrip()) #不空行地输出
    for line in lines:
        print(line.rstrip())
'''
函数open() 接受一个参数:要打开的 文件的名称。Python在当前执行的文件所在的目录中查找指定的
文件。
函数open() 返回一个表示文件的对 象。
Python将这个对象存储在我们将在后面使用 的变量中。
关键字with 在不再需要访问文件后将其关闭,Python自会在合适的时候自动将其关闭。
'''
    


