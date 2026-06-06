#Brian Saville
#June 1, 2026
#Working through Python Crash Course Chapter 8 on functions.

#return values
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = first_name + " " + last_name
    return full_name.title()

musician = get_formatted_name("nancy", "atlas")
print(musician)

#optional values
def get_formatted_name(first_name, last_name, middle_name = ''):
    """Return a full name, neatly formatted."""
    if middle_name: 
        full_name = first_name + " " + middle_name + " " + last_name
    else: 
        full_name = first_name + " " + last_name
    return full_name.title()

musician = get_formatted_name("nancy", "atlas")
print(musician)

musician = get_formatted_name("billy", "cyrus", "ray")
print(musician)

#Passing a List
def yummy_foods(foods):
    """Declares how much I like to eat a list of foods."""
    for food in foods:
        message = "I love to eat " + food + "!!!"
        print(message)

grocery_list = ["peanuts", "raisins", "cheese-its", "baby carrots"]
yummy_foods(grocery_list)

#Modifying a list in a function
def packing(packing_list[:], packed_items): #(:) passes a copy of the list
    """
    Simulates packing items into a suitcase until none are left.
    Move each item to packed_items after packing."""
    while packing_list:
        current_item = packing_list.pop()
        print("Now packing " + current_item + " in suitcase!")
        packed_items.append(current_item)

def show_packed(packed_items):
    """Show all the items packed into suitcase"""
    print("The following items have been packed:")
    for packed_item in packed_items:
        print(packed_item)

packing_list = ["sunglasses", "binoculars", "kindle", "sunscreen", "charger"]
packed_items = []

packing(packing_list, packed_items)
show_packed(packed_items)

#function with an arbitrary number of arguments
    # use an asterisk *before the argument name
    #should come LAST when mixed with positional arguments