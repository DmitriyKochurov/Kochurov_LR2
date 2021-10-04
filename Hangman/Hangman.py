import random

print("HANGMAN")
qw1 = ["python", "java", "javascript", "php"]
qw2 = random.choice(qw1)
qw3 = list(qw2)
print(qw2)
qw0 = input("Guess the word: ")
if qw0 == qw2:
    print("You survived!")
else:
    print("You lose!")
