#Brian Saville
#June 15, 2026
#Working through Chapter 10: files and exceptions of crash course.

#printing the contents of a text files
with open("pi_digits.txt") as file_object:
    contents = file_object.read()
    print(contents)

#the above stores the opened file as file_object
#with = closes file when it is no longer needed
#notice, we open() but do not close()

#file paths
#remember that with windows you need backward slashes
#absolute paths can read from anywhere on your system

#reading line by line
filename = "pi_digits.txt"

with open(filename) as file_object:
    for line in file_object:
        text = line + "...keeping up??"
        print(line.rstrip()) #rstrip removes gaps between the lines

#making a list of lines from a file
with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())

#working with a file's contents
pi_string = ""
for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))

#pi million digits
filename = "pi_million_digits.txt"

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ""
for line in lines:
    pi_string += line.strip()

print(pi_string[:52] + " and so on...")
print(len(pi_string))


#Is your birthday contained in Pi?
birthday = input("Enter your birthday, in the form mmddyy: ")

if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi...")

birthday = input("Enter your birthday, in the form mmddyy: ")

if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi...")