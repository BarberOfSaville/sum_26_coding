#Brian Saville
#June 16, 2026
#10-11: Favorite Number Reader

#Reads the favorite number put into 10-11_favorite_number.py
#and tells the user what it is.

import json

filename = "fav_number.json"
with open(filename) as f_object:
    number = json.load(f_object)

print("A little birdie told me that your favorite number is " + number + "!!")