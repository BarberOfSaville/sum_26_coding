#Brian Saville
#June 11, 2026
#Working through the try it exercises of chapter 9: classes.

#9-1: Restaurant
class Restaurant():
    """A simple attempt to model a restaurant."""

    def __init__(self, name, cuisine_type):
        """Initialize name and cuisine."""
        self.name = name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Prints a message describing the restaurant."""
        print("Welcome to " + self.name.title() + "." +
              " Here we serve " + self.cuisine_type + " food.")
        
    def open_restaurant(self):
        """Prints a message declaring that the restaurant is open."""
        print(self.name.title() + " is now open!!")

mcdonalds = Restaurant("McDonalds", "fast")
mcdonalds.describe_restaurant()
mcdonalds.open_restaurant()


#9-2: Three Restaurants
ihop = Restaurant("ihop", "breakfast")
chipotle = Restaurant("chipotle", "mexican")
panda_express = Restaurant("panda express", "chinese")

ihop.describe_restaurant()
chipotle.describe_restaurant()
panda_express.describe_restaurant()


#9-3: Users
class User():
    """A simple simulation of a user of a site."""
    
    def __init__(self, first_name, last_name, age, sex, fav_movie):
        """Initialize attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.sex = sex
        self.fav_movie = fav_movie

    def describe_user(self):
        """Prints a summary of the user's information."""
        print("NAME: " + self.first_name.title() + " " + 
              self.last_name.title())
        print("AGE: " + str(self.age))
        print("SEX: " + self.sex)
        print("FAVORITE FILM: " + self.fav_movie.title())

    def greet_user(self):
        """Prints a greeting to an inputted user."""
        print("Top o' the mornin', " + self.first_name.title() + 
              " " + self.last_name.title() + "!!!")
        
brian = User("brian", "saville", 26, "male", "whiplash")
ani = User("Annika", "rudolph", "23", "female", "erin brokovich")
peeks = User("MAtthew", "peeks", "25", "male", "Sherlock gnomes")
mom = User("Pattie", "saville", 61, "female", "the sound of music")

User.describe_user(brian)
User.describe_user(ani)
User.greet_user(peeks)
User.greet_user(mom)


#9-4: Number Served

class Restaurant():
    """A simple attempt to model a restaurant."""

    def __init__(self, name, cuisine_type):
        """Initialize name and cuisine."""
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Prints a message describing the restaurant."""
        print("Welcome to " + self.name.title() + "." +
              " Here we serve " + self.cuisine_type + " food.")
        
    def open_restaurant(self):
        """Prints a message declaring that the restaurant is open."""
        print(self.name.title() + " is now open!!")

    def set_number_served(self, number):
        """Sets the number of customers that have been served."""
        self.number_served = number

    def increment_number_served(self, amount):
        """Increments the number of customers by an inputted amount."""
        self.number_served += amount

mcdonalds = Restaurant("McDonalds", "fast")
print(mcdonalds.number_served)

mcdonalds.set_number_served(69)
print(mcdonalds.number_served)

mcdonalds.increment_number_served(67)
print(mcdonalds.number_served)


#9-5: Login Attempts

class User():
    """A simple simulation of a user of a site."""
    
    def __init__(self, first_name, last_name, age, sex, fav_movie):
        """Initialize attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.sex = sex
        self.fav_movie = fav_movie
        self.login_attempts = 0

    def describe_user(self):
        """Prints a summary of the user's information."""
        print("NAME: " + self.first_name.title() + " " + 
              self.last_name.title())
        print("AGE: " + str(self.age))
        print("SEX: " + self.sex)
        print("FAVORITE FILM: " + self.fav_movie.title())

    def greet_user(self):
        """Prints a greeting to an inputted user."""
        print("Top o' the mornin', " + self.first_name.title() + 
              " " + self.last_name.title() + "!!!")
        
    def increment_login_attempts(self):
        """Increases the number of login attempts by 1."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Resets a user's login attempts to 0."""
        self.login_attempts = 0

brian = User("brian", "saville", 26, "male", "whiplash")

brian.increment_login_attempts()
brian.increment_login_attempts()
brian.increment_login_attempts()
brian.increment_login_attempts()
brian.increment_login_attempts()

print(brian.login_attempts)

brian.reset_login_attempts()
print(brian.login_attempts)


#9-6: Ice Cream Stand
class IceCreamStand (Restaurant):
    """Represents aspects of an ice cream stand."""
    def __init__(self, name, cuisine_type):
        """Initialize attributes of the parent class."""
        super().__init__(name, cuisine_type)
        self.flavors = []

    def flavors(self):
        """Displays a list of offered flavors"""
        print(self.name.title() + " serves: " + str(self.flavors))
    
carvel = IceCreamStand("carvel", "ice cream") 
carvel.flavors = ["chocolate", "strawberry", "rocky road", "pistachio"]
IceCreamStand.flavors(carvel)


#9-7: Admin
class Admin(User):
    """Represents an admin, which is a special kind of user."""
    def __init__(self, first_name, last_name, age, sex, fav_movie):
        super().__init__(first_name, last_name, age, sex, fav_movie)
        self.privileges = Privileges()


#9-8: Privileges
class Privileges():
    """List of abilities given to an admin."""
    def __init__(self):
        self.privileges = []

    def give_privileges(self, new_privileges):
        """Grants an admin new privileges."""
        for new_privilege in new_privileges:
            self.privileges.append(new_privilege)

    def show_privileges(self):
        """Prints a list of privileges an admin has."""
        print("This admin has the following privileges:")
        for item in self.privileges:
            print(" -" + item)

    def reset_privileges(self):
        """Takes away an admin's privileges."""
        self.privileges = []
        print("Privileges have been reset.")


peeks = Admin("MAtthew", "peeks", "25", "male", "Sherlock gnomes")
peeks.privileges.give_privileges(["ban users", "can delete posts", "can legally kill users"])
peeks.privileges.show_privileges()

peeks.privileges.reset_privileges()


#9-10: Imported Restaraunt
#yeah no thanks I'm not typing up all the car business


#9-13: OrderedDict Rewrite

from collections import OrderedDict

glossary = OrderedDict()

glossary["append"] = "add to the end of a list"
glossary["dictionary"] = "like a list to store multiple associated values"
glossary["commit"] = "new iteration of a repository"
glossary["elif"] = "portmentaeu of else and if, which describes it well"
glossary["git"] = "version history of your repository"
glossary["loop"] = "iterate through a task repeatedly for different values"
glossary["list"] = "a collection of values stored together"
glossary["boolean"] = "operator storing true/false information"
glossary["python"] = "the programming language I am currently learning"
glossary["key"] = "the information type of a dictionary data point"

for term, meaning in glossary.items():
    print(term.title() + ": " + meaning)


#9-14: Dice
 
from random import randint
x = randint(1, 6)

class Die():
    """Simulates a die that can be rolled for one of a variety of outcomes!"""

    def __init__(self, name, sides):
        """Initializes values"""
        self.name = name
        self.sides = sides

    def roll_die(self):
        """Simulates rolling the die."""
        self.sides = int(self.sides)
        x = randint(1, self.sides)
        print("You rolled a " +str(x) + ".")

    def set_sides(self, newsides):
        """Allow the user to adjust the number of sides on the die."""
        self.sides = newsides
        print("Your dice now has " + str(self.sides) + " sides.")

my_dice = Die("test", 6)
my_dice.roll_die()

ten_sided = Die("10-sided", 10)
ten_sided.roll_die()

twenty_sided = Die("20-sided", 20)
twenty_sided.roll_die()


#9-15: Python Module of the week

#time_ctime.py
import time

print('The time is      :', time.ctime())
later = time.time() + 15
print('15 secs from now :', time.ctime(later))
#wow! This is cool!!