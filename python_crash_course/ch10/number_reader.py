#Brian Saville
#June 16, 2026
#number_reader.py- part of crash course ch10

#for learning json.dump and json.load

import json

filename = "numbers.json"
with open(filename) as f_obj:
    numbers = json.load(f_obj)

print(numbers)