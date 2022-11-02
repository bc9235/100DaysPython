import random
import os

logo = """ _    _ _           _   _       _____ _            _   _                 _             ___  
| |  | | |         | | ( )     |_   _| |          | \ | |               | |           |__ \ 
| |  | | |__   __ _| |_|/ ___    | | | |__   ___  |  \| |_   _ _ __ ___ | |__   ___ _ __ ) |
| |/\| | '_ \ / _` | __| / __|   | | | '_ \ / _ \ | . ` | | | | '_ ` _ \| '_ \ / _ | '__/ / 
\  /\  | | | | (_| | |_  \__ \   | | | | | |  __/ | |\  | |_| | | | | | | |_) |  __| | |_|  
 \/  \/|_| |_|\__,_|\__| |___/   \_/ |_| |_|\___| \_| \_/\__,_|_| |_| |_|_.__/ \___|_| (_) """

EASY_GUESSES = 10
HARD_GUESSES = 5

def check_guess(user_guess, number, guesses):
    """Checks user guess against number, returns number of guesses left."""
    if user_guess > number:
        print("Your guess is too high!  Guess again.")
        return guesses - 1
    elif user_guess < number:
        print("Your guess is too low!  Guess again.")
        return guesses - 1
    else:
        print(f"The number was {number}.  Good job!")
        return

def set_mode():
    """Determine number of guesses allowed."""
    mode = input("Type 'easy' or 'hard' to set difficulty: ").lower()
    if mode == 'easy':
        return EASY_GUESSES
    else:
        return HARD_GUESSES

def play_game():
    print(logo)
    print("\nWelcome to the number guessing game!")
    print("\nI'm thinking of a number between 1 and 100.")
    #Set number of guesses
    guesses = set_mode()
    #Set placeholder for user_guess and play
    play = 'yes'
    user_guess = 0
    while user_guess != number:
        print(f"You have {guesses} guesses left.")
        user_guess = int(input("What is your guess? "))
        guesses = check_guess(user_guess, number, guesses)
        if guesses == 0:
            print("You ran out of guesses.  Game over.")
            return

play = 'yes'
while play == 'yes':
    #Generate number
    number = random.randint(1, 100)
    print(number)
    play_game()
    play = input("Would you like to play again? ").lower()
    if play == 'yes':
        os.system('clear')
