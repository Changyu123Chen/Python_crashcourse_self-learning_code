import json
numbers = [2, 3, 5, 7, 11, 13]
filename = 'text_files/numbers.json'
with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj)
