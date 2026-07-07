#Brian Saville
#June 16, 2026
#Project: make a program that reads a text file and produces a file
    #that's the same, but backwards.

#Prompt user to input file name.
print("Welcome to Brian's text reverser!")
filename = input("Name the text file you wish to reverse (without .txt): ")
true_filename = filename + ".txt"

#Try to locate the file
try:
    with open(true_filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    print("I can't find a file named that.")

#if file is located, proceed.
else:
    #convert string into a list
    backwards_string = contents[::-1]

    #write backward text to file
    new_filename = filename + "_backwards.txt"

    with open(new_filename, "w") as file_object:
        file_object.write(backwards_string)

    #Alert the user what happened.
    print("Success! I've created " + new_filename + ".")

    


