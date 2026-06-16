#Brian Saville
#June 6, 2026

#Made as part of 8-16: Imports to exercise importing a function

def stupid(*things):
    """Declares all inputted items as stupid."""
    for thing in things:
        print(thing + " is stupid!")

stupid("this", "that")