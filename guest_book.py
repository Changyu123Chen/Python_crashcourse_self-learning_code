b = print("Enter your name: (if you wanna quit, please enter 1)")
a = True
while a:
    c = input()
    if c == '1':
        break
    else:
        print("Hello, " + c + '.')
        filename = 'text_files/guest_book.txt'
        with open(filename, 'a') as file_object:
            file_object.write(c + " has entered.\n")

