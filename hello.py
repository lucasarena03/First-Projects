
import random

random.seed()

target = random.randint(1,100)

guess = int(input("Guess: "))

while target != guess:
    if guess > target:
        print("idiot head too high")
    else:
        print("idiot head too low")
    guess = int(input("Guess: "))

print("finally lol u sucked at this")