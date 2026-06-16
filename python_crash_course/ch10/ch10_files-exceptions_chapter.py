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


#replace() Method
message = "I really like cats."
message.replace("cat", "dog")

#WRITING TO A FILE
filename = "writing_test.txt"

with open(filename, "w") as file_object:
    file_object.write("Just wondering if you got those photos printed?")

#writing multiple lines
with open (filename, "w") as file_object:
    file_object.write("Hey, just wondering if you got those photos printed?\n")
    file_object.write("Bogos binted?\n")
    file_object.write("What?\n")

#appending to a file
with open(filename, "a") as file_object:
    file_object.write("*ALIEN EMOJI*\n")
    file_object.write("mysterious...\n")


#EXCEPTIONS
#Allow for user-friendly explanations of errors rather than scary tracebacks

#Handling division by zero
print(5/0)

#Using try-except blocks
try:
    print(5/0)
except ZeroDivisionError:
    print("You sily billy! You know there's no dividing by zero!")
    #and the program continues to run, because we handled the error!

#Using exceptions to prevent crashes

print("Give me two numbers and I will divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == "q":
        break
    second_number = input("\nSecond number: ")
    if second_number == "q":
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("Even I'm not good enough to divide by zero!")
    else:
        print(answer)

#Handling file not found
filename = "no_existe.txt"

try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = "Hmm... doesn't look like " + filename + " really exists..."
    print(msg)


#Analyzing Text
#counting the words in Alice in Wonderland
filename = "alice.txt"

try:
    with open(filename, encoding="utf-8") as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = "Hmm... doesn't look like " + filename + " really exists..."
    print(msg)
else:
    #count the number of words in the file.
    words = contents.split()
    num_words = len(words)
    print("The file " + filename + " has around " + str(num_words) + " words.")


#Working with multiple files
#let's move the above to a word-counting function

def count_words(filename):
    """Count the approximate number of words in a file."""
    try:
        with open(filename, encoding="utf-8") as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        msg = "Hmm... doesn't look like " + filename + " really exists..."
        print(msg)
    else:
        #count the number of words in the file.
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has around " + str(num_words) + " words.")

count_words("alice.txt")
count_words("name.txt")

filenames = ["alice.txt", "bible.txt", "moby_dick.txt", "little_women.txt"]
for filename in filenames:
    count_words(filename)


#Failing silently
#you can use the pass statement to make an error happen silently.

#the same function as above, but with pass instead of an error message
def count_words(filename):
    """Count the approximate number of words in a file."""
    try:
        with open(filename, encoding="utf-8") as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        pass
    else:
        #count the number of words in the file.
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has around " + str(num_words) + " words.")
