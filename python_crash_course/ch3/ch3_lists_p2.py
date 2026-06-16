#Brian Saville
#May 18, 2026
#continuing to work through ch 3 of the python crash course book

#Sort permanently with the sort() Method
safari = ['giraffe', 'elephant', 'lion', 'rhino', 'gazelle', 'aardvark']
safari.sort()
print(safari)

#sort in reverse order
safari.sort(reverse = True)
print(safari)

#Sorted() function: display in an order without actually changing the list
safari = ['giraffe', 'elephant', 'lion', 'rhino', 'gazelle', 'aardvark']
print("Here is the original list:")
print(safari)
print("Here is the sorted list:")
print(sorted(safari))
print("Here is the original order again:")
print(safari)

#reverse order with the reverse() function
safari = ['giraffe', 'elephant', 'lion', 'rhino', 'gazelle', 'aardvark']
print(safari)
safari.reverse()
print(safari)

#finding the length of a list
len(safari)


#TRY IT YOURSELF 3-8: Seeing the world
travel = ["Japan", "Australia", "Germany", "Costa Rica", "Patagonia"]
print(travel)
print(sorted(travel))
print(travel)

#now use sorted to print in reverse alphabetical order
print(sorted(travel, reverse=True))
print(travel)

#use reverse to actually change the order now
travel.reverse()
print(travel)
travel.reverse()
print(travel)

#Use sort() to alphabetize
travel.sort()
print(travel)
travel.sort(reverse= True)
print(travel)


#3-9: Dinner Guests
guests = ['Steve Irwin', 'Obama', 'Robbie Rotten', 'Betty White', 'Steve Vineberg']
numguests = len(guests)
message = "I intend to invite " + str(numguests) + " companions for dinner."
print(message)


#3-10: Every function
rhythm = ['Hole in One', 'See Saw', 'Double Date', 'Air Rally', 'ringside', 'Bossa Nova',
          'Love Rap', 'Tap Troupe', 'Shrimp Shuffle', 'Working Dough']
print(rhythm)
print(rhythm[7])
print(rhythm[4].title())
print(rhythm[-1])
fav = "My favorite game in Rhythm Heaven Fever is " + rhythm[1] + "!"
print(fav)

rhythm[3]= 'Fork Lifter'
print(rhythm)
rhythm.append('Samurai Slice')
print(rhythm)
rhythm.insert(5, 'Packing Pests')
print(rhythm)
del rhythm[0]
print(rhythm)

popped_rhythm = rhythm.pop()
print(rhythm)
print(popped_rhythm)
print("I didn't care for " + popped_rhythm + "...")
popped_rhythm = rhythm.pop(8)
print(popped_rhythm)
print("I'm also not a fan of " + popped_rhythm + "...")
print(rhythm)

rhythm.remove('ringside')
print(rhythm)

rhythm.sort()
print(rhythm)
rhythm = ['Hole in One', 'See Saw', 'Double Date', 'Air Rally', 'ringside', 'Bossa Nova',
          'Love Rap', 'Tap Troupe', 'Shrimp Shuffle', 'Working Dough']
print(sorted(rhythm))
print(rhythm)
rhythm.reverse()
print(rhythm)
rhythm.reverse()
len(rhythm)


#Avoiding index errors when working with lists
feelings = ['happy', 'sad', 'angry']
print(feelings[3])

#Try it yourself: 3-11: intentional error
rhythm = ['Hole in One', 'See Saw', 'Double Date', 'Air Rally', 'ringside', 'Bossa Nova',
          'Love Rap', 'Tap Troupe', 'Shrimp Shuffle', 'Working Dough']
del rhythm[7] #I initially wrote 67, not 7! Sneaky me!

#hehe nice!