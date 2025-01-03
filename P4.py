#Problem 4: Number Guessing Game
#DES: Create a program that plays a guessing game with the user. 
# The program will choose a random number between 1 and 100, and then ask the user to guess the number.
#If the user guesses correctly, the program congratulates the player and ends the game.
#If the user's guess is too high, the program tells them the answer is smaller and lets them guess again.
#If the user's guess is too low, the program tells them the answer is larger and lets them guess again.

import random 

program_loop = True #Trying to make the program loop even after failed user input 

comp = random.randrange(1,100)

guess = int(input(f"Guess a number between 1-100\n>"))

def game():
    if guess == comp:
        print(f"\nCongratulations! you got it right\n")#Getting the right guess
    elif guess < comp:##Guess too low
        print(f"\nYour guess is too low. Try again!\n>")
    
    elif guess > comp:#Guess too high
        print(f"\nYour guess is too high. Try again!\n>")
    return 
    


while program_loop:
    program_loop = game()
    pass