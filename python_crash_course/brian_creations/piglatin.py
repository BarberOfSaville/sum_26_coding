#Brian Saville
#June 16, 2026
#Takes a text file and converts it into piglatin.

#converstion function
def piglatin(word):
    """converts a word into piglatin."""

    #if there's punctuation, cut it to put at the end of a word later.
    punctuation = ".!?,;:'"
    punc_end = ""
    if word[-1] in punctuation:
        punc_end = word[-1]
        word = word[0:-1]

    #If the first letter is capitalized, lowercase it.
    cap_end = False
    if word[0].isupper() and len(word) > 1:
        word = word.lower()
        cap_end = True
    
    #If starts with vowl, add "way"
    vowels = "aeiouAEIOU"
    if word[0] in vowels:
        newword = word + "way"

    #If starts with consonant, put first letter at the end and add "ay"
    else:
        newword = word[1:] + word[0] + "ay"

    #Restore capitalization and punctuation.
    if cap_end:
        return newword.title() + punc_end
    else:
        return(newword) + punc_end

#Prompt user for file and run the function on it.
print("Welcome to the piglatin converter.")
file = input("Please tell me the txt file you wish to convert (Don't type '.txt'): ")
filename = file + ".txt"

with open(filename) as f_obj:
    contents = f_obj.read()
    words = contents.split()

    piglatin_text = []

    for word in words:
        piglatin_text.append(piglatin(word))

    new_text = " ".join(piglatin_text)

newfile = file + "_piglatin.txt"
with open(newfile, "w") as f_obj:
    f_obj.write(new_text)

print("File successfully converted to piglatin!")
