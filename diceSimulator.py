import random

loopAgain = "Y"

while loopAgain == "Y" or loopAgain =="y" :

    diceRoll = random.randint(1,6)

    if diceRoll == 1:
        print(" ---------")
        print("|         |")
        print("|    O    |")
        print("|         |")
        print(" ---------")
    if diceRoll == 2:
        print(" ---------")
        print("| O       |")
        print("|         |")
        print("|       O |")
        print(" ---------")
    if diceRoll == 3:
        print( "---------")
        print("|       O |")
        print("|    O    |")
        print("| O       |")
        print( "---------")
    if diceRoll == 4:
        print(" ---------")
        print("| O     O |")
        print("|         |")
        print("| O     O |")
        print(" ---------")
    if diceRoll == 5:
        print(" ---------")
        print("| O     O |")
        print("|    O    |")
        print("| O     O |")
        print(" ---------")
    if diceRoll == 6:
        print(" ---------")
        print("| O     O |")
        print("| O     O |")
        print("| O     O |")
        print(" ---------")
    else:
        print("Error, not a number from 1 - 6")

    loopAgain = input("Press Y to roll again, any other key to exit: ")