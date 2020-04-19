import random

while True:
    level = int(input("Choose level\n Enter 1, 2 or 3 for Easy, Medium or Hard\n :"))
    if level == 1:
        upper = 10
        count = 6
    elif level == 2:
        upper = 20
        count = 4
    else:
        upper = 50
        count = 3
    generated = random.randrange(1, upper)

    countchecker = 0
    while count != countchecker:

        guessed = int((input("What is your number?: ")))
        if guessed == generated:
            print("You got it right")
            break
        else:
            countchecker += 1
            trials = count-countchecker
            print(f"Wrong guess, you have {trials} guesses left")
            print()

        if count == countchecker:
            print("You have exceeded your number of guesses.")

    retry = input('Do you want to play again?\n Type Y to continue:')
    if retry.lower() != 'y':
        break
    else:
        continue
