#Brian Saville
#June 15, 2026
#Working on the try-it exercises for chapter 10

#10-1: Learning Python

filename = "learning_python.txt"
#print the contents by reading the entire file.
with open(filename) as file_object:
    contents = file_object.read()
    print(contents)

#print the contents by looping over the file
with open(filename) as file_object:
    for line in file_object:
        print(line.strip() + " ...teehee!")

#print the contents by storing the lines in a list
with open(filename) as file_object:
    line_list = []
    for line in file_object:
        line_list.append(line)

print(line_list)


#10-2: Learning C
with open(filename) as file_object:
    for line in file_object:
        print(line.replace("Spotify", "Apple Music"))


#10-3 Guests
guest_name = input("Greetings! Please tell me your name: ")

with open ("guest.txt", "w") as file_object:
    file_object.write(guest_name)


#10-4: Guest Book

active = True
while active:
    print("Greetings! Please tell me your name!")
    guest_name = input("To stop adding names, enter 'q'. ")

    if guest_name == "q":
        active = False
    else:
        guest_name = guest_name + "\n"
        with open("guest_book.txt", "a") as file_object:
            file_object.write(guest_name)

#(from this point on, I switched to doing these exercises in their own files)
#10-6: Addition
print("I am Addatron. Give me two numbers and I will add them.")
number1 = input("Please enter a number: ")
number2 = input("Please enter another number: ")

#convert these numbers to integers
int1 = int(number1)
int2 = int(number2)

#Add the numbers and provide the result
answer = int1 + int2
print(int1 + " plus " + int2 + " equals " + answer + "!!!")

