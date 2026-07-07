#Brian Saville
#June 16, 2026
#10-6: Addition

#Prompt the user for two numbers. 
print("I am Addatron. Give me two numbers and I will add them.")
number1 = input("Please enter a number: ")
number2 = input("Please enter another number: ")

#convert these numbers to integers
try: 
    int1 = int(number1)
    int2 = int(number2)

#if either is not a number, give an error message
except ValueError:
    print("I said give me numbers, silly!")

#otherwise, calculate the solution.
else:

    #Add the numbers and provide the result
    answer = int1 + int2
    print(str(int1) + " plus " + str(int2) + " equals " + str(answer) + "!!!")