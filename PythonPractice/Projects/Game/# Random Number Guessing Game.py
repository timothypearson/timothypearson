# Date 25 Aug 2021
# Mini Python - For Beginners Exercise by #TechwithTim known as Tim Ruscica
# Youtube link: https://www.youtube.com/watch?v=DLn3jOsNRVE&t=1933s

# My Exercise Objectives
    # No.1 write out the code outlined by #TechwithTim exercise
    # No.2 to flag identify what I learnt from each exercise
    # No.3 add my own code commentary to start getting into good habits
    # No.4 Correct or improve code where needed

# My learnings from Tim's Tutorial
    # No.1 - Indent position for functions are important to run code
    # No.2 - Learnt new functions randrange and randint; While loop and elif stateemnt
    # No.3 - break stops look and continue means move back to the top of the loop
    # No.4 - identified a bug / limited in the usage of the isdigit() function.
    # No.5 - I was able to improve the code. A small beginners win in my learning, Hooray!

# Introduction to random functions and ranges

# r = random.randrange(-1, 11) The range only goes from 01 to 10 not 11
# print(r)

# r = random.randint(-5,11) Here, using the int function, it will include 11
# print(r)


# Introduction / Setting up Variables 
# Below I removed the original quit() functions from the tutorial coded example and added a while loop to get the user to return to input question
# Bug: Outstanding bug below to fix 

import random

while True:
top_of_range = input("Type a number: ")  # returns a string

if top_of_range.isdigit():  # isdigit() function checks if user entered a number?
    top_of_range = int(top_of_range)  # convert string to integer using int

    if top_of_range <= 0:    # Bug negative integers are not recognised here because of the isdigit() function only works with positive integers
        print("Please type a number larger than 0 next time.")
        continue
else:
    print("Please type a number next time.")
    continue
break

# Random Number Guessing Game 

random_number = random.randint(0,top_of_range)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Make a guess: ")

    if user_guess.isdigit():  
        user_guess = int(user_guess)  
    else:
        print("Please type a number next time.")
        continue # brings us back to top of loop vs break ends loop

    if user_guess == random_number:
        print("You got it!")
        break
    elif user_guess > random_number:
        print("You were above the number")
    else:
        print("You were below the number!")

# Number Guessing Game Results Summary

print("You got it in", guesses, "guesses") # commas adds spaces & print will convert guesses into int
