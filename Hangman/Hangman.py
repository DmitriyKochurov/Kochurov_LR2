import random

q1 = ["python", "java", "javascript", "php"]
q2 = random.choice(q1)
q3 = set(q2)
try_let = []
wrong = []


def word():
    for letter in q2:
        if letter in try_let:
            print(letter, end='')
        else:
            print('_', end='')


def hang():
    tries = 8
    while tries > 0:
        letter = input("\n")
        if letter in try_let:
            print("You've already guessed this letter!")
            print("")
            word()
            continue
        for i in q2:
            if letter == i:
                try_let.append(letter)
        if letter.capitalize() == letter and len(letter) == 1:
            print("Please enter a lowercase English letter.")
            print("")
            word()
            continue
        if len(letter) == 0 or len(letter) >= 2:
            print("You should input a single letter.")
            word()
            continue
        if letter not in q2:
            wrong.append(letter)
            tries -= 1
            print("That letter doesn't appear in the word")
            if tries == 0:
                print("You lost!")
        print("")
        word()
        if q3 == set(try_let):
            print(" You survived!")
            break


while True:
    answer = input('Type "play" to play the game, "exit" to quit: ')
    if answer == "play":
        print("Try guess the word: ")
        print(len(q2) * '_', end='')
        print("")
        hang()
    elif answer == "exit":
        break