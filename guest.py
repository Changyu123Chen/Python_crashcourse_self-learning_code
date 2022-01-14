filename = 'text_files/guest.txt'
with open(filename, 'w') as file_object:
    file_object.write("Enter your name:\n")
    a = input()
    file_object.write("Hello" + a)
