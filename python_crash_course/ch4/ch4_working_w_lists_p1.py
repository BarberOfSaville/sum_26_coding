#Brian Saville
#May 21, 2026
#working through Chapter 4: Working with Lists in Python Crash Course

stooges = ["larry", "moe", "curly"]
for stooge in stooges:
    print(stooge)
for stooge in stooges:
    print(stooge.title() + " is a pretty funny guy.")
    print("I can't wait to hear your next joke, " + stooge.title() + "!\n")
print("Thank you for being 3 funny stooges.")

#Try it yourself
#4-1: Pizzas
pizzas = ["pepperoni", "buffalo", "margherita", "pineapple"]

for pizza in pizzas:
    print("I make-a da " + pizza + " now! Mamma mia!")
print("Look at all of da pizza I made! *chef's kiss*")


#4-2: Animals
animals = ["parrot", "bat", "mantis"]
for animal in animals:
    print("Did you know that a " + animal + " has wings?")
print("Lots of animals can fly!")


#Making numerical lists
for value in range(1, 40):
    print(str(value) + " Mississippi!")
print("Ready or not, here I come!")

#turning numbers into a list
numbers = list(range(1,7))
print(numbers)

#you can do a lot with the range function.
#here, we make a list of the first 10 squares
squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)
print(squares)

#functions for lists of numbers
min(squares)
max(squares)
sum(squares)

#Try it yourself

#4-3: Counting to Twenty
onetotwenty = list(range(1,21))
for number in onetotwenty:
    print(number)
print("See? I CAN count to twenty!")

#4-4: One million
million = list(range(1, 1000001))
for number in million:
    print(str(number) + " banana peels...")
print("That's a lot of peels!")

#4-5: Summing a million
million = list(range(1, 1000001))
min(million)
max(million)
sum(million)

#4-6: Odd numbers
odd_numbers = list(range(1, 21, 2))
for oddnumber in odd_numbers:
    print(oddnumber)
print("Did I forget any numbers?")

#4-7: Threes
threes = list(range(3, 31, 3))
for three in threes:
    print(three)
print("I can count by threes!")

#4-8: Cubes
cubes = []
for value in range(1, 11):
    cubes.append(value**3)
for cube in cubes:
    print(cube)
print("Like my cubes???")

#4-9: Cube comprehension
cubes = [value**3 for value in range(1,11)]
print(cubes)