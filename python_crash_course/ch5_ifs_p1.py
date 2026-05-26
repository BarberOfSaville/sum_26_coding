#Brian Saville
#May 26, 2026
#Working through chapter 5 of Python crash course on if statements

#circumventing case sensitivity
car = "Audi"
car.lower() == 'audi' #gives back True regardless of case
car

#checking whether a value is in a list
requested_toppings = ["bacon", "spinach", "anchovies"]
"bacon" in requested_toppings
"nerds" in requested_toppings

#checking whether a value is NOT in a list
zoo_animals = ["penguin", "kangaroo", "giraffe"]
animal = "cheetah"

if animal not in zoo_animals:
    print(animal.title() + " is not a creature we have at the zoo.")

#TRY IT YOURSELF!!
#5-1: conditional tests
drink = "Water"
print("Are you drinking water? I sure hope so.")
print(drink.lower() == "water")

print("You better not be drinking a beer instead!")
print(drink.lower() == "beer")

#5-2: more conditional tests
magic_num = 39
print("What number am I think of?")
print("Tell me, is it greater than 12?")
print(magic_num > 12)
print("Well then, is it bigger than 100?")
print(magic_num > 100)
print("Hmm... smaller than 70?")
print(magic_num <= 70)
print("Bigger than 50?")
print(magic_num >= 50)
print("Bigger than 20?")
print(magic_num >= 20)
print("Well then... is it 39??")
print(magic_num == 39)

#test whether an item is on a list
fears = ["spiders", "clowns", "heights", "holes"]
"clowns" in fears
"darkness" in fears

#test whether item is not in a list
fear = "frogs"
if fear not in fears:
    print("No, I'm not afraid of " + fear)


#If/Else/Elif statements
age = 32
if age < 18:
    print("You cannot vote or drink. Lame.")
elif age < 21:
    print("You can vote but not buy beer. So close!")
else:
    print("You can do whatever you want. Enjoy your freedom!")

#testing multiple conditions
#if you only want run block to run, use if=elif-else
#if multiple blocks need to run, use a series of independent ifs

#Try it yourself
#5-3: Alien Colors #1
alien_colors = ["green", "yellow", "red"]
alien_color = "yellow"
if alien_color == "green":
    print("You just earned five points!")

#5-4: Alien colors 2
alien_color = "green"
if alien_color == "green":
    print("You earned 5 points!")
else:
    print("Wow! You earned 10 points!")

#5-5: Alien colors 3
alien_color = "blue"
if alien_color == "green":
    print("You eanred 5 points.")
elif alien_color == "yellow":
    print("You earned 10 points!")
elif alien_color == "red":
    print("You earned 15 points!!!")

#5-6: Stages of Life
age = 200
if age < 2:
    print("You are a baby.")
elif age < 4:
    print("You are a toddler.")
elif age < 13:
    print("You are a child.")
elif age < 20:
    print("You are a teenager.")
elif age < 65:
    print("You are an adult.")
elif age >= 65:
    print("You are a senior citizen.")

#5-7: Favorite Fruit
favorite_fruits = ["banana", "clementine", "grape"]
fruit = "clementine"
if fruit in favorite_fruits:
    print("You must really like " + fruit + "!!")
else: 
    print("Not much of a " + fruit + " fan, huh?")


#Using if statements with lists

requested_toppings = ["mushrooms", "green peppers", "extra cheese"]
for requested_topping in requested_toppings:
    if requested_topping == "green peppers":
        print("Sorry, we are out of green peppers right now.")
    else: 
        print("Adding " + requested_topping + ".")

print("Finished making your pizza!")

#Checking that a list is not empty
requested_toppings = []
#when the name of a list is in an if statement:
#   returns true if not empty
#   returns false if not empty

#using multiple lists
available_toppings = ["mushrooms", "olives", "green peppers", 
                      "pepperoni", "pineapple", "extra cheese"]
requested_toppings = ["mushrooms", "french fries", "extra cheese"]

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + " to pizza.")
    else: 
        print("Sorry, we don't have " + requested_topping + ".")

print("All finished making your pizza!")

#TRY IT YOURSELF
#5-8: Hello Admin
users = ["admin", "brian", "billy", "annika", "kira"]
for user in users:
    if user == "admin":
        print("Hello, " + user + "! You're looking sexy today.")
    else:
        print("Good afternoon, " + user + ".")

#5-9: No Users
users = ["admin", "brian", "billy", "annika", "kira"]

users = ["jeff", "admin", "james"]
if users:
    for user in users:
        if user == "admin":
            print("Hello, " + user + "! You're looking sexy today.")
        else:
            print("Good afternoon, " + user + ".")
else:
    print("We really need some users for this site!")


#5-10: Checking Usernames
current_users = ["Butcher", "Hughie", "Frenchie", "MM", "Kimiko"]

#make a new list of all usernames in lowercase
current_users_lower = []
for current_user in current_users:
    current_users_lower.append (current_user.lower())
current_users_lower

#add new users
new_users = ["Annie", "Sage", "BUTCHER", "mm", "Homelander"]

#check to see if these new usernames are available (case sensitive)
for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print("Sorry, that username is already taken.")
    else:
        print("That username is available!")

    
#5-11: Ordinal Numbers
numbers = list(range (1,10))

for number in numbers:
    if number == 1:
        print(str(number) + "st")
    elif number == 2:
        print(str(number) + "nd")
    elif number == 3:
        print(str(number) + "rd")
    elif number > 3:
        print(str(number) + "th")


#Styling your if statements