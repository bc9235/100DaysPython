import pandas

# Import data from CSV
nato_data = pandas.read_csv("nato_phonetic_alphabet.csv")

# Create dictionary from CSV data
nato_dict = {row.letter: row.code for (index, row) in nato_data.iterrows()}

print("Welcome to the NATO Alphabet Converter!")

run = True
while run:
  # User input
  user_word = input("What word would you like to convert?\n").upper()
  try:
    # Create new list by looping letters in user word
    user_converted = [nato_dict[letter] for letter in user_word]
  except KeyError:
    print("Sorry, only letters in the alphabet please.")
  else:
    print(f"Your conversion:\n{user_converted}")
    run = False
