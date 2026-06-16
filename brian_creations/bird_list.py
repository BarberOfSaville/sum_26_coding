#Brian Saville
#June 1, 2026
#Tooling around with Python after Ch7 of Crash Course

#Greet the user
print("Welcome to the Life List tracker.")

#Generate prompt for user input.
prompt = "Name a species of bird that you've seen."
prompt += "\n(If you're done naming species, type 'end'.) "

#Generate dictionary
life_list = {}
input_active = True

#Prompt user to input birds and places until they wish to stop
while input_active:
    #Prompt the user to input a bird species and location
    bird = input(prompt)

    #stop if the user inputs "end"
    if bird == "end":
        break

    location = input("Where did you see this bird? ")

    #Store that bird in a list
    life_list[bird] = location

#Show the user their life list
print("\nHere is your life list:\n")

num = 1
for bird, location in life_list.items():
    print(str(num) + ". " + bird.title() + ", first seen at "
           + location.title())
    num += 1

print("\nYou have " + str(num) + " birds on your life list.")