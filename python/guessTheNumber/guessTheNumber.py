import random
from asyncore import loop
from random import randrange

print("From what range do you want to guess? ")
rangeLength1 = int(input("First bound: "))
rangeLength2 = int(input("Second bound: "))

number = randrange(rangeLength1, rangeLength2 + 1)

guess = int(input("Guess? "))

while guess != number: 
    if guess < number:
        print("Higher...")
    if guess > number: 
        print("Lower...")
    guess = int(input("Guess again? "))
else: 
    print("Congratulations! You've guessed correctly!")

