#Brian Saville
#June 16, 2026
#number_writer.py- part of crash course ch10

#for learning json.dump and json.load

import json

numbers = [4, 2, 0, 7, 1, 0, 6, 9, 6, 7, 3, 9]

filename = "numbers.json"
with open(filename, "w") as f_obj:
    json.dump(numbers, f_obj)