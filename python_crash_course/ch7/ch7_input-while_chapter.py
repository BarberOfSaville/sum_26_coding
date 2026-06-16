#Brian Saville
#May 27, 2026
#Python Crash Course Ch. 7: User Input and While Loops
#Chapter Work

#print the user's text back to them:
message = input("Tell me the password: ")
print(message)

name = input("What's your name? Tell me: ")
print("Top o' the mornin', " + name + "!!")

#writing longer prompts by storing the message as a variable
prompt = "If you tell me your name, I can treat you with hospitality."
prompt += "\nSo, what is your first name? "

name = input(prompt)
print("\nHey there, " + name + ".")

#Accepting numerical input
#User input is always a string- it will need to be converted to int
age = input("How old are you? ")
age = int(age)

if age >= 21:
    print("You can buy beer! Yippee!!!")
elif age < 21:
    print("Sorry! Come back when you're older!")

#the Modulo operator
#divides a number by another and returns the remainder

#Using this to determine if a number is even or odd
number = input("Gimme a number and I'll tell you if it's odd or even: ")
number = int(number)

if number % 2 == 0:
    print("That number is even-steven!")
else: 
    print("That number is one odd fellow.")


#Introducing WHILE LOOPS
#while loops run for as long as certain conditions are true.

current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

#letting the user choose when to quit
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = ""

active = True
while active:
    message = input(prompt)
    if message == "quit":
        active = False
    else:
        print(message)

#Using a flag- see above where I've updated it

#Using break to Exit a loop
prompt = "Tell me about the places you've visited!"
prompt += "\n(Enter 'quit' when you're all done.) "

while True:
    city = input(prompt)
    if city == "quit":
        break
    else: 
        print("I'd love to go to " + city.title() + "!!")

#Start a while with TRUE: it runs forever until you hit a BREAK statement
#this works in any loop type

#Using continue in a loop
#continue returns to the beginning of a loop (skipping the rest of it)

#example: print only odd numbers:
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)


#Using a while loop with lists and dictionaries
#can use a while loop to have a user modify a list or dictionary

#moving from one list to another
unconfirmed_users = ["annika", "brian", "carl"]
confirmed_users = []

while unconfirmed_users: #runs while unconfirmed_users is not empty
    current_user = unconfirmed_users.pop()

    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)

print("The following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

#Remove all instances of specific valyes in a list
pets = ["dog", "dog", "dog", "cat", "cat", "cat", "cat",
        "fish", "fish", "lizard", "rabbit", "cat"]
print(pets)

while "cat" in pets:
    pets.remove("cat")
    print("Cat's outta the bag!")

print(pets)

#Filling a dictionary with user input
responses = {}

#indicate that polling is active
polling_active = True

while polling_active:
    #Prompt the user for a name and response.
    name = input("What is your name?")
    color = input("What is your favorite color?")

    #store responses in the dictionary
    responses[name] = color

    #Find out if more people will take the poll
    repeat = input("Would anyone else like to respond? (yes/no) ")
    if repeat == "no":
        polling_active = False

#polling complete. Show results:
print("--- Poll Results---")
for name, response in responses.items():
    print(name + " likes the color " + response + ".")