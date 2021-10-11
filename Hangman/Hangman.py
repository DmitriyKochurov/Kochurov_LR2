import random

print("""HANGMAN
Try guess word:""")

q1 = ["python", "java", "javascript", "php"]
q2 = random.choice(q1)


def hang():
    let = ''
    tries = 8
    while tries > 0:
        misses = 0
        for letter in q2:
            if letter in let:
                print(letter, end=' ')
            else:
                print('_', end=' ')
                misses = misses + 1
        guess = input('')
        if guess.capitalize() == guess and len(guess) == 1:
            print("Please enter a lowercase English letter.")
            print("")
        if len(guess) == 0 or len(guess) >= 2:
            print("You should input a single letter.")

        if misses == 0:
            print("You survived!")
            break

        guess = input('')
        let += guess
        if guess not in q2:
            tries -= 1
            print("That letter doesn't appear in the word")
            if tries == 0:
                print("You lost!")


hang()