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
