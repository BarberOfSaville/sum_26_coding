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
    print(name.title() + " would like to go to " + response.title()
          + "!")
