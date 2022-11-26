from tkinter import *
from random import choice
import pandas

GREEN = "#B1DDC6"
LANGUAGE_FONT = ("Arial", 30, "italic")
WORD_FONT = ("Arial", 50, "bold")


def new_card():
    """Pick a random entry from list of pairs.  Display on card.  Flip the card."""
    global current_card, timer
    window.after_cancel(timer)
    current_card = choice(words)
    canvas.itemconfig(color, image=card_front)
    canvas.itemconfig(title, text="French", fill="black")
    canvas.itemconfig(definition, text=current_card["French"], fill="black")
    timer = window.after(5000, flip_card)


def flip_card():
    """Flip the card over."""
    canvas.itemconfig(color, image=card_back)
    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(definition, text=current_card["English"], fill="white")


def known_card():
    """Remove entry from word list.  Generate new card."""
    words.remove(current_card)
    new_card()


def save_exit():
    """Save unknown words to new file.  Close window."""
    window.after_cancel(timer)
    data = pandas.DataFrame(words)
    data.to_csv("data/words_to_learn.csv", index=False)
    window.destroy()


# Dictionary to hold current card
current_card = {}

# Set up Window
window = Tk()
window.title("Flashcards")
window.config(padx=25, pady=25, bg=GREEN)
timer = window.after(5000, flip_card)

# Set up Canvases
canvas = Canvas(width=800, height=526, bg=GREEN, highlightthickness=0)
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
color = canvas.create_image(400, 263, image=card_front)
title = canvas.create_text(400, 100, text="", font=LANGUAGE_FONT)
definition = canvas.create_text(400, 263, text="", font=WORD_FONT)
canvas.grid(column=0, row=0, columnspan=3)

# Set up Buttons
known = PhotoImage(file="images/right.png")
known_button = Button(image=known, command=known_card, highlightthickness=0)
known_button.grid(column=2, row=1)

unknown = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=unknown, command=new_card, highlightthickness=0)
unknown_button.grid(column=0, row=1)

# Save & Exit Button
exit_button = Button(text="Save & Exit", command=save_exit, bg=GREEN, height=5, width=15, highlightthickness=0)
exit_button.grid(column=1, row=1)

# Import CSV Data and Make Dictionary with data
try:
    # See if there is words_to_learn file
    words = pandas.read_csv("data/words_to_learn.csv")
    words = words.to_dict(orient="records")
except FileNotFoundError:
    # If no words_to_learn.csv, use french_words.csv
    words = pandas.read_csv("data/french_words.csv")
    words = words.to_dict(orient="records")
finally:
    # Generate first card
    new_card()

window.mainloop()
