#Problem 4: Number Guessing Game
#DES: Create a program that plays a guessing game with the user. 
# The program will choose a random number between 1 and 100, and then ask the user to guess the number.
#If the user guesses correctly, the program congratulates the player and ends the game.
#If the user's guess is too high, the program tells them the answer is smaller and lets them guess again.
#If the user's guess is too low, the program tells them the answer is larger and lets them guess again.

import random 

comp = random.randrange(1,100)

guess = int(input(f"Guess a number between 1-100\n>"))

def game():
    
    if guess == comp:
        print(f"\nCongratulations! you got it right\n")
    elif guess < comp:
        print(f"\nYour guess is too low. Try again!\n>")
    