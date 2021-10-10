import random

print("""HANGMAN
Try guess word:""")

qw1 = ["python", "java", "javascript", "php"]
qw2 = random.choice(qw1)
let = ''
tries = 8

while tries > 0:
    misses = 0
    for letter in qw2:
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
    if guess not in qw2:
        tries -= 1
        if tries == 0:
            print("You lost!")