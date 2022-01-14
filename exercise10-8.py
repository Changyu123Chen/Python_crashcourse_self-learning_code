def readfile(filename):
    
    try:
        with open(filename, 'r') as f_obj: #写在try里面
            contents = f_obj.read()

    except FileNotFoundError:
        pass
        #print("The file cannot be found.")
    else:
        print(contents)

filename1 = "text_files/cats.txt"
filename2 = "text_files/dogs.txt"
filename3 = "dogs.txt" #不存在
readfile(filename1)
readfile(filename2)
readfile(filename3)
