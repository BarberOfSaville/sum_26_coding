#Brian Saville
#June 6, 2026
#part of the chapter 8 lesson on importing modules

def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print("Making a " + str(size) +
          "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)