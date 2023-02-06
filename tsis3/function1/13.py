'''Write a program able to play the "Guess the number" - game, 
where the number to be guessed is randomly chosen between 1 and 20.'''

import random

def guess_number(number, name):
    right_number = random.randint(1,20)
    count = 1
    while number != right_number :
        if number > right_number:
            print("Your guess is too big.")
        elif number < right_number:
            print("Your guess is too low.")
        print("Take a guess.")
        count += 1
        number = int(input())
    print("Good job,",name,"! You guessed my number in",count,"guesses!")


print("Hello! What is your name?")
name = input()
print("Well,",name,",I am thinking of a number between 1 and 20.")
print("Take a guess.")
number = int(input())
guess_number(number, name)