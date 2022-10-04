import random
import math

print("Welcome to Roots and Powers (only integer answers)! ")

def game():
    operatorValue = input("What operator do you want to practice? ")
    amountCorrect = []

    if operatorValue == "roots":
        root = int(input("What root do you want to practice? "))
        power = 1/root
        
    if operatorValue == "powers":
        power = int(input("What power do you want to practice? "))

    problemCount = int(input("How many problems do you want? "))

    print("From what range do you want to practice? ")

    range1 = int(input("First range:"))
    range2 = int(input("Second range:"))

    for i in range(problemCount):
        baseNumber = random.randint(range1, range2)
        
        if power < 1:
            baseNumber = baseNumber**root

        actualAnswer = math.ceil(baseNumber**power)

        if power < 1:
            userAnswer = int(input(f"{baseNumber} ^ (1/{root}) = "))
        else:
            userAnswer = int(input(f"{baseNumber} ^ {power} = "))

        if userAnswer == actualAnswer:
            print("Correct!")
            amountCorrect.append("1")
        else:
            print("Incorrect!")

    percentCorrect = len(amountCorrect) * 100 / problemCount
    print(f"\nYou got {percentCorrect}%!")

    gameContinue = input("Do you want to continue (y/n)? ")

    if gameContinue == "y":
        game()

game()

input("end")

