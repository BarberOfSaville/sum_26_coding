#Brian Saville
#June 11, 2026
#Working through Matthes chapter 9: classes.

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

my_dog = Dog("cooper", 1)
print("My parent's dog is " + my_dog.name.title() + ".")
print("Their dog is " + str(my_dog.age) + " years old.")