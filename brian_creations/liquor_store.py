#Brian Saville
#May 27th, 2026

#Prompt user to input their age
age = input("How old are you? ")

#convert to int
age = int(age)

#Deliver the output
if age >= 21:
    print("You can buy beer! Yippee!!!")
elif age >= 18:
    print("Almost there! At least you can vote.")
elif age < 18:
    print("Sorry! You can't buy beer for a while!")

#Extra comment for old-timers
if age >= 100:
    print("Also, wow! You're quite the old-timer!")