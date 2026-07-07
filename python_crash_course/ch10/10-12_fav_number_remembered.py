#Brian Saville
#June 16, 2026
#10-12: Favorite Number Remembered

#combines the two 10-11 files into one
import json

def get_new_number():
    """Gathers the user's favorite number."""
    number = input("Tell me, what is your favorite number? ")

    #store number to a json file
    filename = "ch10/fav_number.json"
    with open(filename, "w") as file_object:
        json.dump(number, file_object)
    print("I'll tell everyone your favorite number is " + number + "!!")
    return number

def get_existing_number():
    """Retreives stored favorite number"""
    filename = "ch10/fav_number.json"
    try:
        with open(filename) as f_object:
            number = json.load(f_object)
        return number
    except FileNotFoundError:
        return None

def tell_number():
    """Talks to the user, whether it knows the number or not."""
    filename = "ch10/fav_number.json"
    number = get_existing_number()
    if number:
        print("A little birdie told me that your favorite number is " + number + "!!")
    else:
        get_new_number()


tell_number()
