import random

while True:
    try:
        level = int(input("Level: "))
        if (level >= 1):
            break
    except ValueError:
        pass

rando = random.randint(1, level)

while True:
    try:
        guess = int (input("Guess: "))
        if (guess >= 1):
            if (guess == rando):
                print("Just right!")
                break
            elif (guess > rando):
                print("Too large!")
            elif (guess < rando):
                print("Too small!")
    except ValueError:
        pass
    except EOFError:
        pass