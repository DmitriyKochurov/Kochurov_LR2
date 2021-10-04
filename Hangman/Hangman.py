import random

print("HANGMAN")
qw1 = ["python", "java", "javascript", "php"]
qw2 = random.choise(qw1)
print(qw2)
qw0 = input("Guess the word")
if qw0 == qw2
    print("You survived!")
else:
    print("You lose!")
