import json
filename = "text_files/favorite_number.json"
with open(filename, 'r') as f:
    number = json.load(f)
    print("I know your favorite number! It's " + number)
