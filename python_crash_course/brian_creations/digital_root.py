#Brian Saville
#May 27, 2026
#playing around after Chapter 7 work.
#Asks user for a number and gives the number's digital root.

#Prompt user to input a number
number = input("Please give me a number: ")

#Convert number to a string of digits
digits = list(number)

sum = 100

#Keep adding the digits together until total is less than 10
while sum >= 10:
    sum = 0
    for digit in digits:
        number = int(digit) #convert digits to integers
        sum += number #add digits to sum
    digits = list(str(sum)) #create new digit list 

print("Your digital root is " + str(sum) + ".")






