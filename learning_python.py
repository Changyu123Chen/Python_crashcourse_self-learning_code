with open('text_files/learning_python.txt') as file_object:
    lines = file_object.readlines()
    print(lines)
    
    for line1 in file_object:
        print(line1.rstrip())

    contents = file_object.read()
    print(contents)

    
