#Brian Saville
#June 16, 2026
#10-11: Favorite Number

#Prompts the user for a favorite number
#Saves the number as a json

import json

number = input("Tell me, what is your favorite number? ")

#store number to a json file
filename = "fav_number.json"
with open(filename, "w") as file_object:
    json.dump(number, file_object)

print("I'll tell everyone your favorite number is " + number + "!!")