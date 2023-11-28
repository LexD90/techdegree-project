"""
Data Analysis Techdegree
Project 1 - A Number Guessing Game
--------------------------------
"""

import random
import statistics
from statistics import mean, mode, median

#not in range formula/code taken from https://www.tutorialkart.com/python/python-range/python-if-in-range/#gsc.tab=0
#this was in an attempt to keep away code smell by not having another elif for both more than and less than.

attempts_list = []

# This function contains the core game mechanics, generating the random number, checking if it is too high or low and also checking for errors.
def start_game():
    #   1. Display an intro/welcome message to the player.
    print(f"*** Welcome to the number guessing game! *** \nA number has been generated! Guess the number between 1-10. Good luck!\n")
    high_score()
    #   2. Store a random number as the answer/solution.
    MASTER_NUMBER = random.randint(1,10)
    attempt = 0
    #   3. Continuously prompt the player for a guess.
    while True:
        try:
            guess = int(input("\nPlease enter your guess:  "))
            # Checking if the guess is in the range - this means I only need one formula for checking if the number is too high or too low.
            if guess not in range(1,11):
               print("Your guess needs to be between 1 - 10. Try again \n  ")
               attempt += 1
               continue
            elif guess > MASTER_NUMBER:
                 print("It's lower\n ")
                 attempt += 1
                 continue
            elif guess < MASTER_NUMBER:
                 print("It's higher\n ")
                 attempt += 1
                 continue
            else:
                attempt += 1
                attempts_list.append(attempt)
                got_it()
        # Checking for errors that are not numeric. The below statement covers anything that isn't an integer.
        except ValueError as err:
            print("ERROR: Please only use whole numbers. This attempt will not count. Please try again.")
            continue
        # This allows the user to play again, and resets the random number and shows the high score!
        play_again = input("Do you want to play again? Y/N    ")
        if play_again.lower() == "y":
            MASTER_NUMBER = random.randint(1, 10)
            attempt = 0
            print(f"\nYour high score (lower is better) is {min(attempts_list)} attempts")
            continue
        elif play_again.lower() == "n":
            print("\nThanks for playing my first ever game! Come back soon!")
            break

# The below function covers the mathematics of the users scores
def got_it():
    print("Got it\n")
    print(f"It took {attempts_list[-1]} attempts to complete this challenge")
    print(f"Your average number of attempts: {mean(attempts_list)} ")
    print(f"Median number of attempts: {median(attempts_list)} ")
    print(f"Mode number of attempts: {mode(attempts_list)} \n")


#This function calculates high score
def high_score():
    if len(attempts_list) == 0:
        print("You don't have a high score yet - play a few games to build it up!")
    else:
        print(f"Your high score (lower is better) is {min(attempts_list)} attempts")



start_game()
