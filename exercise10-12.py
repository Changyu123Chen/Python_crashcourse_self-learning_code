import json
def get_number_stored():
    filename = "text_files/favorite_number.json"
    try:
        with open(filename) as f:
            number = json.load(f)
    except ValueError:
        number = input("Enter your favorite number: \n")
        number = str(number)
        filename = "text_files/favorite_number.json"
        with open(filename, 'w') as f:
            number = json.dump(number, f)
            return number
    else:
        return number

number = get_number_stored()
print("I know your favorite number! It's "+ str(number))
