#Brian Saville
#May 27, 2026
#Python Crash Course Ch. 7: User Input and While Loops
#Try it Yourself

#7-1: Rental Car
car = input("What type of car are you looking to rent? ")
print("I'll check the garage and see if we have a " + car + ".")


#7-2: Restaurant Seating:
prompt = "Welcome to Chili's. \nHow many are we today? "
party = input(prompt)

party = int(party)
if party >= 8:
    print("You will have to wait for a table.")
else:
    print("Great! Right this way, please.")


#7-3: Multiples of Ten
number = input("Quick! Gimme a number! ")

number = int(number)
if number % 10 == 0:
    print("Wowza! That's a multiple of 10 right there!")
else:
    print("Yikes! That's not a multiple of 10...")


#7-4: Pizza Toppings
prompt = "Welcome to Peppino's Pizza! \nWhat toppings would you like? "
topping = " "

while True:
    topping = input(prompt)
    if topping == "quit":
        print("Thank you for choosing Peppino's Pizza!")
        break
    print(topping.title() + " will be yummy on your pizza!")


#7-5: Movie Tickets
prompt = "Welcome to AMC Theaters! My name is Nicole Kidman."
prompt += "\nHow old are you? (Enter 'quit' to exit.) "

while True:
    age = input(prompt)
    if age == "quit":
        print("See you next time at AMC Theaters!")
        break
    age = int(age)
    price = 0
    if age < 3:
        price = 0
    elif age <= 12:
        price = 10
    elif age > 12:
        price = 15
    
    if price == 0:
        print("Your ticket is free, little one!")
    else:
        print("Your ticket will cost " + str(price) + " dollars.")


#7-6: Three Exits

#Break
prompt = "Welcome to Peppino's Pizza! \nWhat toppings would you like? "
topping = " "

while True:
    topping = input(prompt)
    if topping == "quit":
        print("Thank you for choosing Peppino's Pizza!")
        break
    print(topping.title() + " will be yummy on your pizza!")

#Conditional Test
prompt = "Welcome to Peppino's Pizza! \nWhat toppings would you like? "
topping = " "

while topping != "quit":
    topping = input(prompt)
    if topping == "quit":
        print("Thank you for choosing Peppino's Pizza!")
        continue
    print(topping.title() + " will be yummy on your pizza!")

#Active variable
prompt = "Welcome to Peppino's Pizza! \nWhat toppings would you like? "
topping = " "
active = True

while active == True:
    topping = input(prompt)
    if topping == "quit":
        print("Thank you for choosing Peppino's Pizza!")
        active = False
        continue
    print(topping.title() + " will be yummy on your pizza!")


#7-7: Infinite Loop
number = 1
while number == 1:
    print("The ride never stops!")


#7-8: Deli
sandwich_orders = ["tuna", "salami", "blt", "grilled cheese", "marmalade"]
finished_orders = []

while sandwich_orders:
    current_order = sandwich_orders.pop()

    print("I'm making the " + current_order + " sandwich now!")
    finished_orders.append(current_order)

print("Whew! I just made these sandwiches:")
for order in finished_orders:
    print("\tA " + order + " sandwich!")


#7-9: No Pastrami
sandwich_orders = ["tuna", "salami", "pastrami", "blt", "grilled cheese", 
                   "pastrami", "marmalade", "pastrami", "pastrami"]
finished_orders = []

print("Welcome to Shirley's Sandwiches!")
print("Heads up-- we are all out of pastrami today! Sorry!")

while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")
    print("Again, we have no pastrami! Sorry folks.")

while sandwich_orders:
    current_order = sandwich_orders.pop()

    print("I'm making the " + current_order + " sandwich now!")
    finished_orders.append(current_order)

print("Whew! I just made these sandwiches:")
for order in finished_orders:
    print("\tA " + order + " sandwich!")


#7-10: Dream Vacation
responses = {}
polling_active = True


while polling_active:
    #prompt the user for a name and response
    name = input("What is your name? ")
    response = input("If you could vacation anywhere, where" \
                     "would you go? ")
    
    #store responses in the dictionary
    responses[name] = response

    #Find out if more people are answering
    repeat = input("Do more people want to answer? (yes/no) ")
    if repeat == "no":
        polling_active = False

#Show results when polling is complete
print("--- Survey Results ---")
for name, response in responses.items():
    print(name.title() + " would like to go to " + response.title())

