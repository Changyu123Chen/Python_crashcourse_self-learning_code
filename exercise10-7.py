while True:
    number1 = input("Please enter a number: \n")
    number2 = input("Please enter another numbers: \n")
    try:
        int(number1)
        int(number2)
    except ValueError:
        print("You entered the wrong type.")
    else:
        print(number1 + " " + number2)
    
