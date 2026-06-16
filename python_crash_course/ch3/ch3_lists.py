#Brian Saville
#May 18, 2026

#Ch 3 of Python Crash Course: playing with lists
fruits = ['mango', 'guava', 'clementine', 'durian', 'dragonfruit', 
          'banana', 'apple', 'persimmon', 'avocado', 'tomato', 'starfruit',
            'grape']
print(fruits)

print(fruits[7])
print(fruits[9].title())

#be wary of indexes starting at 0
print(fruits[3]) #will print the fourth fruit
print(fruits[-1]) #will print the last item in a list

#pulling an item from a list to concatenate
message = "The yummiest fruit there is is a " + fruits[5].title() + "!!!"
print(message)

#3-1: Names
names = ['Peeks', 'Angelica', 'Obi', 'Jason', 'Matt', 'Siobhan', 'Nat', 'Em']
#print each name, one at a time
print(names[0])
print(names[1])
print(names[2])
print(names[3])
print(names[4])
print(names[5])
print(names[6])
print(names[-1])

#3-2: Greetings
message = "Good to see ya, " + names[0] + ", old sport!"
print(message)
message = "Good to see ya, " + names[1] + ", old sport!"
print(message)
message = "Good to see ya, " + names[5] + ", old sport!"
print(message)
message = "Good to see ya, " + names[-1] + ", old sport!"
print(message)

#3-3: Your own list
subways = ['A', 'B', 'C', 'D', '1', '2', '3', '4', '5', '6']
message = "I waited for the " + subways[0] + " train for so darned long!"
print(message)


#Modifying elements in a list
names = ['Peeks', 'Angelica', 'Obi', 'Jason', 'Matt', 'Siobhan', 'Nat', 'Em']
print(names)
names[0] = 'The esteemed Mr. Matthew Peeques, esquire'
print(names)

#Appending items to list
friends = ['Pim', 'Charlie', 'Allan', 'Glep']
print(friends)
friends.append('Mr. Boss')
print(friends)

#inserting elements into a list
friends = ['Pim', 'Charlie', 'Allan', 'Glep']
friends.insert(2, 'Jombo')
print(friends)

#removing items from list with the del statement
friends = ['Pim', 'Charlie', 'Jombo', 'Allan', 'Glep']
print(friends)
del friends[2]
print(friends)

#removing items using the pop() method
friends = ['Pim', 'Charlie', 'Allan', 'Glep', 'Mr. Boss']
print(friends)
popped_friends = friends.pop()
print(friends)
print(popped_friends) #stores the values that have been popped from the list

#pop an item from anywhere on the list
friends = ['Pim', 'Charlie', 'Allan', 'Glep', 'Mr. Boss']
fired = friends.pop(1)
print("I'm going to have to let one of you go. " + fired + ", you're fired.")
print(friends)
#Use pop() if you want to use an item as you remove it.

#Remove a value by item
friends = ['Pim', 'Charlie', 'Allan', 'Smormu', 'Glep', 'Mr. Boss']
print(friends)
friends.remove('Smormu')
print(friends)

friends = ['Pim', 'Charlie', 'Allan', 'Smormu', 'Glep', 'Mr. Boss']
fake_friend = 'Smormu'
friends.remove(fake_friend)
print(friends)
print(fake_friend + " is not fifth Smiling Friend material")


#Try it Yourself
#3-4: Guest List
guests = ['Steve Irwin', 'Obama', 'Robbie Rotten', 'Betty White', 'Steve Vineberg']
invite = "Dear " + guests[0] + ", you are cordially invited to my dinner party."
print(invite)
invite = "Dear " + guests[1] + ", you are cordially invited to my dinner party."
print(invite)
invite = "Dear " + guests[2] + ", you are cordially invited to my dinner party."
print(invite)
invite = "Dear " + guests[3] + ", you are cordially invited to my dinner party."
print(invite)
invite = "Dear " + guests[4] + ", you are cordially invited to my dinner party."
print(invite)


#3-5: Changing guest list
update = "I have just been informed that " + guests[1] + " can no longer join us."
print(update)

guests.remove('Obama')
guests.insert(1, 'Bruce Springsteen')
invite = "Dear " + guests[1] + ", you are cordially invited to my dinner party."
print(invite)


#3-6: More Guests
guests.insert(0, 'Kim Hale')
guests.insert(3, 'Kermit the Frog')
guests.append('Harambe')
print(guests)
invite = "Dear " + guests[0] + ", you are cordially invited to my dinner party."
print(invite)
invite = "Dear " + guests[3] + ", you are cordially invited to my dinner party."
print(invite)
invite = "Dear " + guests[-1] + ", you are cordially invited to my dinner party."
print(invite)


#3-7: Shrinking the guest list
print("I fear that I can only accomodate two guests this evening. Apologies.")
uninvited = guests.pop()
message = "Dear " + uninvited + ", I am so sorry, but you are uninvited from the party."
print(message)
uninvited = guests.pop()
message = "Dear " + uninvited + ", I am so sorry, but you are uninvited from the party."
print(message)
uninvited = guests.pop()
message = "Dear " + uninvited + ", I am so sorry, but you are uninvited from the party."
print(message)
uninvited = guests.pop()
message = "Dear " + uninvited + ", I am so sorry, but you are uninvited from the party."
print(message)
uninvited = guests.pop()
message = "Dear " + uninvited + ", I am so sorry, but you are uninvited from the party."
print(message)
uninvited = guests.pop()
message = "Dear " + uninvited + ", I am so sorry, but you are uninvited from the party."
print(message)

message = "Dear " + guests[0].title() + ", I am happy to report that you can still come tonight."
print(message)
message = "Dear " + guests[1].title() + ", I am happy to report that you can still come tonight."
print(message)

del guests[1]
del guests[0]
print(guests)