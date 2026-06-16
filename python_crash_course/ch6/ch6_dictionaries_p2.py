#Brian Saville
#May 27, 2026
#continuing to learn Python with Ch6 of Crash Course

#TRY IT YOURSELF
#6-4: Glossary 2
glossary = {"append" : "add to the end of a list",
            "dictionary" : "like a list to store multiple associated values",
            "commit" : "new iteration of a repository",
            "elif" : "portmentaeu of else and if, which describes it well",
            "git" : "version history of your repository",
            "loop" : "iterate through a task repeatedly for different values",
            "list" : "a collection of values stored together",
            "boolean" : "operator storing true/false information",
            "python" : "the programming language I am currently learning",
            "key" : "the information type of a dictionary data point",}
#print the definitions
for term, meaning in glossary.items():
    print(term.title() + ": " + meaning)

#6-5: Rivers
rivers = {"amazon" : "brazil", "hudson" : "u.s.a.", "thames" : "england"}
for river, country in rivers.items():
    if country != "u.s.a.":
         print("Did you know the " + river.title() + " river runs through " +
             country.title() + "?")
    elif country == "u.s.a.":
        print("Did you know the " + river.title() + " river runs through the " +
             country.title() + "?")

print("The following rivers have been mentioned:")
for river in rivers.keys():
    print(river.title())
print("The following countries have been mentioned:")
for country in rivers.values():
    print(country.title())


#6-6: Polling
favorite_languages = {
    "brian": "python",
    "annika" : "c", 
    "angelica" : "matlab",
    "obi" : "python",
}

should_take_poll = ["peeks", "nat", "emily", "annika", "obi", "spiros"]

for person in should_take_poll:
    if person in favorite_languages.keys():
        print("Thanks for taking the poll, " + person.title() + "!!")
    else:
        print("Hey " + person.title() + ", you should take our poll!")


#Nesting
#storing dictionaries in lists and lists in dictionaries
monster_0 = {"type" : "fire", "attack" : 5}
monster_1 = {"type" : "water", "attack" : 10}
monster_2 = {"type" : "grass", "attack" : 15}

monsters = [monster_0, monster_1, monster_2]

for monster in monsters:
    print(monster)

#above, we manually generated 3 enemeies and looped through them.
#more realisitcally, could automatically generate.
monsters = []

#make the monsters
for monster_number in range(30):
    new_monster = {"type" : "fire", "attack" : 5, "defense" : 7}
    monsters.append(new_monster)

#show the first few monsters
for monster in monsters[:7]:
    print(monster)
print("...")

#show how many monsters we've made
print("Total monster count: " + str(len(monsters)))

#modifying elements already in the list
for monster in monsters[0:3]:
    if monster["type"] == "fire":
        monster["type"] = "electric"
        monster["attack"] = 10
        monster["defense"] = 10

#show the first few monsters
for monster in monsters[:7]:
    print(monster)
print("...")

#dictionaries in a list ex:
#   each user is a dictionary, and all users are stored in a list

#A LIST in a DICTIONARY!
#example: pizza

pizza = {
    "crust" : "thick",
    "toppings" : ["mushrooms", "extra cheese"],
}

print("You ordered a " + pizza["crust"] + "-crust pizza " +
      "with the following toppings:")
for topping in pizza["toppings"]:
    print("\t" + topping)

#A dictionary in a dictionary
#you can do it, but it can get complicated fast
users = {
    "sirwin" : {
        "first": "steve",
        "last" : "irwin",
        "location" : "australia",
    },
    "aearhart" : {
        "first" : "amelia",
        "last" : "earhart",
        "location" : "unknown",
    },
    "bobama" : {
        "first" : "barack",
        "last" : "obama",
        "location" : "chicago",
    },
}

for username, user_info in users.items():
    print("\nUsername: " + username)
    full_name = user_info["first"] + " " + user_info["last"]
    location = user_info["location"]

    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())


#TRY IT YOURSELF
#6-7: New People
annika = {"first_name" : "Annika", "last_name" : "Rudolph",
           "age" : 23, "location" : "Manhattan",}
kira = {"first_name" : "Kira", "last_name" : "Stone",
           "age" : 25, "location" : "Hawaii",}
peeks = {"first_name" : "Matthew", "last_name" : "Peeks",
           "age" : 25, "location" : "Queens",}

people = [annika, kira, peeks]

for person in people:
    print("Full name: " + person["first_name"] + " " +
          person["last_name"])
    print("\tAge: " + str(person["age"]))
    print("\tLocation: " + person["location"])


#6-8: Pets
cooper = {"name" : "cooper", "animal" : "dog", "owner" : "mom/dad",}
rudy = {"name" : "rudy", "animal" : "rabbit", "owner" : "serena",}
pippa = {"name" : "pippa", "animal" : "cat", "owner" : "grace",}
camouflage = {"name" : "camouflage", "animal" : "parakeet", "owner" : "peeks",}

pets = [cooper, rudy, pippa, camouflage]

for pet in pets:
    print("\nName: " + str(pet["name"]).title())
    print("\tAnimal: " + str(pet["animal"]).title())
    print("\tOwner: " + str(pet["owner"]).title())


#6-9: Favorite Places
favorite_places = {
    "brian" : ["central park", "bronx zoo"],
    "annika" : ["fort tryon", "the met", "central park"],
    "peeks" : ["astoria park", "nxt legaci"],
    "grace" : ["the met"],
}

for name, places in favorite_places.items():
    print("\nName: " + name.title())
    print("Favorite places: ")
    for place in favorite_places[name]:
        print(str(place).title())


#6-10: Favorite Numbers
fav_numbers = {"brian" : [39, 5, 12], 
               "annika" : [12, 23], 
               "peeks" : [67], 
               "sam" : [30, 39, 99, 72], 
               "mom" : [61, 1964],}

#print everybody's favorite numbers
for name, numbers in fav_numbers.items():
    print("\nName: " + name.title())
    print("Favorite numbers: ")
    for number in fav_numbers[name]:
        print("\t" + str(number))


#6-11: Cities
cities = {
    "new york" : {
        "country" : "U.S.A.",
        "population" : 8500000,
        "fact" : "I live here",
    },
    "london" : {
        "country" : "United Kingdom",
        "population" : 9100000,
        "fact" : "They have bad teeth here",
    },
    "paris" :{
        "country" : "France",
        "population" : 2400000,
        "fact" : "It's the city of love",
    },
}

for city, city_info in cities.items():
    print("\nCity: " + str(city).title())
    print("\tCountry: " + city_info["country"])
    print("\tPopulation: " + str(city_info["population"]))
    print("\tFun Fact: " + city_info["fact"])


#6-12: Extensions
