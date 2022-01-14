import json
number = input("Enter your favorite number:\n")
number = str(number)
filename = "text_files/favorite_number.json"
with open(filename, 'w') as f:
    json.dump(number, f)

