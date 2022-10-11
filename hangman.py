import random
import hangman_words
import hangman_art
import os

chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)
end_of_game = False
lives = 6

print(hangman_art.logo)

#Create blanks
display = []
guess_list = []

for point in range(word_length):
    display += "_"

while not end_of_game:
  guess = input("Guess a letter: ").lower()
  os.system('clear')
  print(hangman_art.logo)
  #If the user has entered a letter they've already guessed, print the letter and let them know.
  if guess in guess_list:
    print(f'You have already guessed {guess}.')
  else:
    guess_list += guess
    #Check guessed letter
    for point in range(word_length):
        char = chosen_word[point]
        if char == guess:
          display[point] = guess
    

    #Check if user is wrong.
    if guess not in chosen_word:
        print(f'{guess} is not in the word.')
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win!")
      
  print(hangman_art.stages[lives])