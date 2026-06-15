#Brian Saville
#June 15, 2026
#A copy of the restaurant class in a separate module
#for practing importing modules (in ch. 9)

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