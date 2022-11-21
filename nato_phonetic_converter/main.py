import pandas

# Import data from CSV
nato_data = pandas.read_csv("nato_phonetic_alphabet.csv")

# Create dictionary from CSV data
nato_dict = {row.letter: row.code for (index, row) in nato_data.iterrows()}

# User input
print("Welcome to the NATO Alphabet Converter!")
user_word = input("What word would you like to convert?\n").upper()

# Create new list by looping letters in user word
user_converted = [nato_dict[letter] for letter in user_word]

print(f"Your conversion:\n{user_converted}")
