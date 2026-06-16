#Brian Saville
#May 27, 2026
#Collects names and favorite colors until the user says quit

responses = {}

#indicate that polling is active
polling_active = True

while polling_active:
    #Prompt the user for a name and response.
    name = input("What is your name? ")
    color = input("What is your favorite color? ")

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