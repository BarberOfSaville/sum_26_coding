#Brian Saville
#May 22, 2026
#Continuing to work through Chapter 4 of Python Crash Course

#slicing a list
things = ['pencil', "scissors", "tape", "sticky notes", "cup", "moose"]
print(things[0:3])
print(things[1:4])
print(things[:2]) #first two items
print(things[2:]) #skip the first two items

#output the last three items on the list
print(things[-3:])

#looping through a slice
print("Here are the first three items on my desk:")
for thing in things[:3]:
    print(thing.title())
print("So yeah, those are the first three things I saw on the desk")

#copying a list
my_movies = ['Knives Out', "Eternal Sunshine", "Babe 2"]
ani_movies = my_movies[:]

my_movies.append("Godzilla Minus One")
ani_movies.append("Father of the Bride")

print("My favorite movies are:")
print(my_movies)

print("Ani's favorite movies are DEFINITELY:")
print(ani_movies)

#Try it yourself
#4-10: Slices
persons = ["Ace", "Snake", "Santa", "Clover", "Junpei", "June", "Seven", 
           "Lotus", "9th Man"]
print("The first three persons are:")
for person in persons[:3]:
    print(person)
print("The middle three persons are:")
for person in persons[3:6]:
    print(person)
print("The last three persons are:")
for person in persons[-3:]:
    print(person)
print("Which persons will survive the game?")


#4-11: My pizzas, your pizzas
pizzas = ["pepperoni", "buffalo", "margherita", "pineapple"]

for pizza in pizzas:
    print("I make-a da " + pizza + " now! Mamma mia!")
print("Look at all of da pizza I made! *chef's kiss*")

friends_pizzas = pizzas[:]

pizzas.append("veggie")
friends_pizzas.append("mushroom")

print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)
print("\nMy friend's favorite pizzas are:")
for friends_pizza in friends_pizzas:
    print(friends_pizza)
print("We all love different kinds of pizza.")


#4-12: More loops
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

print("My favorite foods are:")
for my_food in my_foods:
    print("I like " + my_food + "!")
print("\nMy friend's favorite foods are:")
for friend_food in friend_foods:
    print("My buddy likes " + friend_food + "!")
print("Our tastes differ ever so slightly.")


#Tuples
#a TUPLE is like a list that cannot change. It is immutable.

#for example, dimensions of a rectangle
dimensions = (60, 70)
print(dimensions[0])
print(dimensions[1])

#you can loop through a tuple too:
for dimension in dimensions:
    print(dimension)
print("hehe 67")

#writing over a tuple
print("original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 20)
print("\n Modified Dimensions:")
for dimension in dimensions:
    print(dimension)


#Try it yourself
#4-13: Buffet
menu = ("burger", "taco", "crepe", "soup", "quesadilla")
for item in menu:
    print(item)
print("That's our menu!")

#try changing a value in a tuple
menu[1] = "corn dog"

#rewrite the tuple for a new menu
menu = ("burger", "sushi", "crepe", "soup", "noodles")
for item in menu:
    print(item)
print("And that's our new menu!")