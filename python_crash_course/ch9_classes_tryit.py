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