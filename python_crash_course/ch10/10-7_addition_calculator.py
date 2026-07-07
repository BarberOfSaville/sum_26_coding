#Brian Saville
#June 16, 2026
#10-7: Addition Calculator

#Prompt user for numbers. 
print("I am Addtar the Great! I know how to add the values of TWO numbers!!!")
numbers_input = []

while len(numbers_input) < 2:
    number1 = input("Please enter a number: ")
    try: 
        int1 = int(number1)
        numbers_input.append(int1)
    except ValueError:
        print("I can only add numbers.")
        pass

answer = sum(numbers_input)
print(str(numbers_input[0]) + " plus " + str(numbers_input[1]) + 
      " equals " + str(answer) + "!!!")

