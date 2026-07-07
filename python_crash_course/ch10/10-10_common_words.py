#Brian Saville
#June 16, 2026
#10-10: Common Words
#Counts the number of times an inputted word is present in a text file

filename= "ch10/pride_and_prejudice.txt"
#prompt the user to input the word
buzzword = input("Tell me the word you'd like to count: ")

word_count = 0

#Count the number of instances of the word on each line
    #and increment the counter accordingly
with open(filename, encoding="utf-8") as file_object:
    for line in file_object:
        word_count += line.lower().count(buzzword)

#Print the results
print("The word '" + buzzword + "' appears " + str(word_count) +
      " times in the file " + filename + "!!!")
