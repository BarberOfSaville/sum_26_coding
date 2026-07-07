#June 16, 2026
#part of ch10- learning json 

import json

#Load the username, if it has been stored previously.
#Otherwise, prompt for the username and restore it.

#also added 10-13: Verify user, to make sure it's the same person.

def get_stored_username():
    """Get stored username if available"""
    filename = "username.json"
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username
    
def get_new_username():
    """Prompts the user for a new name."""
    username = input("What is your name? ")
    filename = "username.json"
    with open(filename, "w") as f_obj:
        json.dump(username, f_obj)
    return username

def greet_user():
    """Greets the user by name."""
    filename = "username.json"
    username = get_stored_username()
    if username:
        print("Greetings! Is this " + username + "?")
        same_user = input("(Enter 'yes' or 'no'.) ")
        if same_user.lower() == "yes":
            print("Welcome back, " + username + "!")
        else:
            username = get_new_username()
            print("We'll remember you when you come back, " + username + "!")

greet_user()