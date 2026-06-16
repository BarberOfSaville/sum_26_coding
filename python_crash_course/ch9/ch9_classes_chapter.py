#Brian Saville
#June 11, 2026
#Working through Matthes chapter 9: classes.

#creating the class Dog
class Dog():
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command"""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(self.name.title() + " rolled over!")

#accessing attributes of Dog
my_dog = Dog("cooper", 1)
print("My parent's dog is " + my_dog.name.title() + ".")
print("Their dog is " + str(my_dog.age) + " years old.")

#calling methods of Dog
my_dog.sit()
my_dog.roll_over()

#working with classes and instances
class Pokemon():
    """A simple attempt to respresnt a Pokemon."""

    def __init__(self, name, number, type1, type2):
        """Initalize attributes of the Pokemon."""
        self.name = name
        self.number = number
        self.type1 = type1
        self.type2 = type2
        self.level = 1
    
    def description(self):
        """Return a description of the Pokemon."""
        blurb = str(self.number) + ". " + self.name.title() + " (" + self.type1.title() + "/" + self.type2.title() + ")"
        return(blurb)
    
    def check_level(self):
        """Print a statement showing the Pokemon's level."""
        print(self.name.title() + " Lv. " + str(self.level))

    def level_up(self, amount):
        """Increase the Pokemon's level by a given value."""
        self.level += amount

    def set_level(self, level):
        """Change the Pokemon's level to a given value."""
        self.level = level

bewear = Pokemon("bewear", 760, "normal", "fighting")
print(bewear.description())
bewear.check_level()

#modifying attribute values
#1. modifying directiy
bewear.level = 25
bewear.check_level()

#2. modifying through a method
bewear.set_level(50)
bewear.check_level()

#3. incrementing through a method
bewear.level_up(6)
bewear.check_level()


#Inheritance
#making a class that takes attributes from an existing class

class UltraBeast(Pokemon):
    """Represents aspects of a Pokemon, specific to Ultra Beasts."""
    
    def __init__(self, name, number, type1, type2):
        """Initialize attributes of the parent class."""
        super().__init__(name, number, type1, type2)
        self.attack = 100

    def give_attack(self):
        """Print a statement describing attack power."""
        print(self.name.title() + " has an Attack stat of " + str(self.attack) + ".")

buzzwole = UltraBeast("buzzwole", 794, "bug", "fighting")
print(buzzwole.description())
buzzwole.give_attack()


#Classses from the Python Standard Library
#example: Ordered Dict

from collections import OrderedDict

favorite_animal = OrderedDict()

favorite_animal["brian"] = "elephant"
favorite_animal["annika"] = "giraffe"
favorite_animal["nat"] = "snow leopard"
favorite_animal["emily"] = "bat"

for name, animal in favorite_animal.items():
    print(name.title() + "'s favorite animal is a " +
          animal + ".")