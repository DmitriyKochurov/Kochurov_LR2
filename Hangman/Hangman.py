import random

print("""HANGMAN
Try guess word:""")

q1 = ["python", "java", "javascript", "php"]
q2 = random.choice(q1)
let = ''
tries = 8

while tries > 0:
    misses = 0
    for letter in q2:
        if letter in let:
            print(letter,end=' ')
        else:
          print('_',end=' ')
          misses = misses + 1

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