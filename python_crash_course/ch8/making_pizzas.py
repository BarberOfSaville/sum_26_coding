#Brian Saville
#June 6, 2026
#part of the chapter 8 lesson on importing modules

import pizza #imports all functions from pizza.py

pizza.make_pizza(16, "pepperoni")
pizza.make_pizza(12, "mushrooms", "green peppers", "triple poop")


#alternatively, could import only SOME functions from a file
from pizza import make_pizza

#for us right now, this should have the same effect.
#because we called make_pizza specifically, no need for the dot notation.
make_pizza(16, "pepperoni")
make_pizza(12, "mushrooms", "green peppers", "triple poop")


#Using as to give a function an alias
from pizza import make_pizza as mp
mp(16, "pepperoni")
mp(67, "sprinkles", "chocolate", "twizzlers")


#Import all functions in a module
#(not really recommended, they could conflict with your own code)
from pizza import *

make_pizza(39, "candy corn")