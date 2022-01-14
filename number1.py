import json
filename = 'text_files/number1.json'
with open(filename) as f:
    number = json.load(f)

    print(number)
