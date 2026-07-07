#Brian Saville
#June 16, 2026
#10-8: Cats and Dogs/ 10-9: Silent Cats and Dogs

#print items from the cats file
filename1 = "ch10/cats.txt"

try:
    with open(filename1) as file_object:
        print("\n")
        for line in file_object:
            print(line.strip())
except FileNotFoundError:
    #print("The file " + filename1 + " does not exist.")
    pass

#print items from the dogs files
filename2 = "ch10/dogs.txt"

try:
    with open(filename2) as file_object:
        print("\n")
        for line in file_object:
            print(line.strip())
except FileNotFoundError:
    #print("The file " + filename2 + " does not exist.")
    pass
