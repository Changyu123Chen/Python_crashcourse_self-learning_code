filename = 'text_files/pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.rstrip()

print(pi_string[2:5])#遇到有很多数字的文件，无需全部输出，可以截取部分输出
print(len(pi_string[2:5]))

a = '4'
if a in pi_string:
    print("Yes")
else:
    print("no")
    
