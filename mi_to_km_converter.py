from tkinter import *


def conversion():
    """Get user input and convert miles to kilometers rounded to two decimal places."""
    # Convert user_input to float
    user_input = float(entry.get())
    # Round answer to two decimal places
    km = round(user_input * 1.609344, 2)
    # Replace km_answer_label with new answer
    km_answer_label.config(text=km)


# Window setup
window = Tk()
window.title("Miles to KM Converter")
window.config(padx=50, pady=50)

# Entry box for user input
entry = Entry(width=5, justify=CENTER)
entry.grid(column=1, row=0)

# Labels
miles_label = Label(text="mi")
miles_label.grid(column=2, row=0)

equal_label = Label(text="equal to")
equal_label.grid(column=0, row=1)

km_answer_label = Label(text="")
km_answer_label.grid(column=1, row=1)

kilometer_label = Label(text="km")
kilometer_label.grid(column=3, row=1)

# Button
convert = Button(text="Convert!", command=conversion)
convert.grid(column=1, row=3)

window.mainloop()
