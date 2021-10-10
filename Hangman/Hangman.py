import random

print("HANGMAN")

qw1: list[str] = ["python", "java", "javascript", "php"]
qw2 = random.choice(qw1)
lena = len(qw2[2:-1])

your_word = ''
start = str(input())

print("Guess the word")
print(qw2[:3] + '-' * lena)
your_word = str(input(" guess the word > "))
if your_word == qw2:
    print("You win!")
else:
    print("You lost")