# Date 25 Aug 2021
# Mini Python - For Beginners Exercise by #TechwithTim known as Tim Ruscica
# Youtube link: https://www.youtube.com/watch?v=DLn3jOsNRVE&t=1933s


# My Exercise Objectives
    # No.1 write out the code outlined by #TechwithTim exercise
    # No.2 to flag identify what I learnt from each exercise
    # No.3 add my own code commentary to start getting into good habits


# My learnings from Tim's Tutorial
    # No.1 python syntax is case sensitve and use tabs instead of spaces
    # No.2 usage of the input function and if / else statement
    # No.3 IDLE is installed with python and is the interactive shell to execute the code 
    
    
# Introduction

print("Welcome to my computer quiz!")

playing = input("Do you want to play? ").lower()

if playing.lower() != "yes":
	quit()  

print("Okay! Let's play :) ")
score = 0

# Start Quiz - 5 Questions

# Question 1

answer = input("What does CPU stand for? ").lower()

if answer == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

# Question 2

answer = input("What does GPU stand for? ").lower()

if answer == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

# Question 3

answer = input("What does RAM stand for? ").lower()

if answer == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

# Question 4

answer = input("What does PSU stand for? ").lower()

if answer == "power supply unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

# Quiz Game Results Summary
print("You got " + str(score) + " questions correct!")
print("You got " + str((score/4)*100) +"%" + " correct!")
