import random

print("Welcome to Basic Operators!\n")

def game():
    operator = input("What operator do you want to practice? ")

    def game_addition():
        problemCount = int(input("How many problems do you want (enter a numerical value)? "))
        digits1 = int(input("How many digits do you want the first number to be (enter a numerical value)? "))
        digits2 = int(input("How many digits do you want the second number to be (enter a numerical value)? "))

        digitRange1 = 10**(digits1-1)
        digitRange2 = (10**(digits1))-1

        digitRange3 = 10**(digits2-1)
        digitRange4 = (10**(digits2))-1

        amountCorrect = []

        for i in range(problemCount):
            firstNumber = random.randint(digitRange1, digitRange2)
            secondNumber = random.randint(digitRange3, digitRange4)
            actualSum = firstNumber + secondNumber

            userSum = int(input(f"{firstNumber} + {secondNumber} = "))   
            
            if userSum == actualSum:
                print("Correct!")
                amountCorrect.append("1")
            else: 
                print("Incorrect!")

        percentCorrect = len(amountCorrect) * 100 / problemCount

        print(f"You got {percentCorrect}%!")

        gameContinue = input("\nDo you want to continue (y/n)? ")

        if gameContinue == "y": 
            game()

    def game_subtraction():
        problemCount = int(input("How many problems do you want (enter a numerical value)? "))
        digits1 = int(input("How many digits do you want the first number to be (enter a numerical value)? "))
        digits2 = int(input("How many digits do you want the second number to be (enter a numerical value)? "))

        digitRange1 = 10**(digits1-1)
        digitRange2 = (10**(digits1))-1

        digitRange3 = 10**(digits2-1)
        digitRange4 = (10**(digits2))-1

        amountCorrect = []

        for i in range(problemCount):
            firstNumber = random.randint(digitRange1, digitRange2)
            secondNumber = random.randint(digitRange3, digitRange4)
            actualSum = firstNumber - secondNumber

            userSum = int(input(f"{firstNumber} - {secondNumber} = "))   
            
            if userSum == actualSum:
                print("Correct!")
                amountCorrect.append("1")
            else: 
                print("Incorrect!")

        percentCorrect = len(amountCorrect) * 100 / problemCount

        print(f"You got {percentCorrect}%!")

        gameContinue = input("\nDo you want to continue (y/n)? ")
        
        if gameContinue == "y": 
            game()

    def game_multiplication():
        problemCount = int(input("How many problems do you want (enter a numerical value)? "))
        digits1 = int(input("How many digits do you want the first number to be (enter a numerical value)? "))
        digits2 = int(input("How many digits do you want the second number to be (enter a numerical value)? "))

        digitRange1 = 10**(digits1-1)
        digitRange2 = (10**(digits1))-1

        digitRange3 = 10**(digits2-1)
        digitRange4 = (10**(digits2))-1

        amountCorrect = []

        for i in range(problemCount):
            firstNumber = random.randint(digitRange1, digitRange2)
            secondNumber = random.randint(digitRange3, digitRange4)
            actualSum = firstNumber * secondNumber

            userSum = int(input(f"{firstNumber} * {secondNumber} = "))   
            
            if userSum == actualSum:
                print("Correct!")
                amountCorrect.append("1")
            else: 
                print("Incorrect!")

        percentCorrect = len(amountCorrect) * 100 / problemCount

        print(f"You got {percentCorrect}%!")

        gameContinue = input("\nDo you want to continue (y/n)? ")
        
        if gameContinue == "y": 
            game()

    def game_division():
        problemCount = int(input("How many problems do you want (enter a numerical value)? "))
        digits1 = int(input("How many digits do you want the first number to be (enter a numerical value)? "))
        digits2 = int(input("How many digits do you want the second number to be (enter a numerical value)? "))

        digitRange1 = 10**(digits1-1)
        digitRange2 = (10**(digits1))-1

        digitRange3 = 10**(digits2-1)
        digitRange4 = (10**(digits2))-1

        amountCorrect = []

        for i in range(problemCount):
            firstNumber = random.randint(digitRange1, digitRange2)
            secondNumber = random.randint(digitRange3, digitRange4)
            actualSum = firstNumber / secondNumber

            userSum = int(input(f"{firstNumber} / {secondNumber} = "))   
            
            if userSum == actualSum:
                print("Correct!")
                amountCorrect.append("1")
            else: 
                print("Incorrect!")

        percentCorrect = len(amountCorrect) * 100 / problemCount

        print(f"\nYou got {percentCorrect}%!")

        gameContinue = input("\nDo you want to continue (y/n)? ")
        
        if gameContinue == "y": 
            game()
            
    if operator == "addition":
        game_addition()
    
    if operator == "subtraction":
        game_subtraction()

    if operator == "multiplication":
        game_multiplication()

    if operator == "division":
        game_division()
    
game()

input("end")