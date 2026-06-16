#Brian Saville
#June 1, 2026
#Working on the try it exercises for Ch8: Functions of Python Crash Course

#8-1: Message
def message():
    """Displays a message about what I'm making."""
    print("In this chapter, I'm learning about functions!")

message()


#8-2: Favorite Book
def favorite_book(title):
    """Prints a statement about an inputted book title."""
    print("I've had " + title + " sitting on my shelf forever!")

favorite_book("Demon Copperhead")


#8-3: T-shirt
def tshirt(size = "L", color = "blue", message = "Life is Good"):
    """Prints a statement about a shirt of a chosen size and message."""
    print("I'm looking for a " + color + ", size " + size + " t-shirt.")
    print('Printed on the shirt is the message: "' + message + '".')

tshirt("small", "red", "bogos binted?")
tshirt(color = "green", size = "XXL", message = "Virginia is for lovers")


#8-4: Large shirts
def tshirt(size = "large", color = "blue", message = "I love Python!"):
    """Prints a statement about a shirt of a chosen size and message."""
    print("I'm looking for a " + color + ", size " + size + " t-shirt.")
    print('Printed on the shirt is the message: "' + message + '".')

tshirt(color = "pink")
tshirt("medium", "yellow")
tshirt("extra small", message = "Tangela Fan Club")


#8-5: Cities
def describe_city(city = "Reykjavik", country = "Iceland"):
    """"Prints a statement about a given city and its home country."""
    print("I am going on a voyage to " + city + ", " + country + "!!!")

describe_city("New York", "USA")
describe_city(city = "Melbourne", country = "Australia")
describe_city("Tokyo", country = "Japan")


#8-6: City Names
def city_country(city = "New York", country = "United States"):
    """Neatly prints a city and its country."""
    city_country = city.title() + ", " + country.title()
    print(city_country)

city_country("munich", "germany")
city_country("Yokohama", "japan")
city_country("qUiTO", "ECUADOR")


#8-7: Album
def make_album(artist = "The Beatles", title = "Abbey Road", tracks = 0):
    """Stores and artist and album title in a dictionary"""
    if tracks != 0:
        album = {"artist" : artist, "title" : title, "tracks" : tracks}
    else:
        album = {"artist" : artist, "title" : title}
    return album

make_album("Taylor Swift", "reputation", 8)
make_album("Brian and the Savilles", "bird city")
make_album("Billy Joel", "piano man")


#8-8: User Albums
while True:
    print("Welcome! Name a musical artists.")
    print("Enter 'q' to quit at any time.")
    user_artist = input("Artist: ")

    if user_artist == "q":
        break

    print("Now, name one of their albums.")
    user_title = input("Enter 'q' to quit at any time. ")

    if user_title == "q":
        break

    album_dictionary = make_album(user_artist, user_title)
    print(album_dictionary)


#8-9 Magicians
def show_magicians(magician_roster):
    """Prints the name of each magician in a list."""
    for magician in magician_roster:
        print("Pulling " + magician + " out of a hat!")

magician_alliance = ["GOB Bluth", "Tony Wonder", "Uncle Magic", "Quopstromboli"]
show_magicians(magician_alliance)


#8-10: Great Magicians + 8-11: Unchanged Magicians
def make_great (magician_roster):
    """Adds 'the great' to the name of each magician in a list."""
    magician_roster = [magician + " the Great"
                       for magician in magician_roster]
    return magician_roster

great_alliance = make_great(magician_alliance)
show_magicians(great_alliance)
show_magicians(magician_alliance)

#alternatively, can use ennumerate to modify the original list


#8-12: Sandwiches
def sandwich (*ingredients):
    """Collects a list of ingredients and prints a summary of the sandwich."""
    print("The customer would like a sandwich with the following ingredients:")
    for ingredient in ingredients:
        print("- " + ingredient)
    print("\nSounds like a yummy sandwich!")

sandwich("bacon", "lettuce", "tomato", "chicken", "mayo")


#8-13: User profile
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user"""
    profile = {}
    profile["first_name"] = first
    profile["last name"] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile("brian", "saville", location = "new york",
                             undergrad = "Holy Cross", grad = "Fordham", 
                             high_school = "Regis")

print(user_profile)


#8-14: Cars
def make_car(manufacturer, model_name, **car_info):
    """Builds a dictionary of information about a car"""
    car = {}
    car["manufacturer"] = manufacturer
    car["model"] = model_name
    for key, value in car_info.items():
        car[key] = value
    return car

car = make_car("subaru", "outback", color = "pink", tow_package = True)
print(car)


#8-16: Imports
import is_stupid
print(is_stupid.__file__)
is_stupid.stupid("this", "that", "nintendo", "the government")