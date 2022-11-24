from tkinter import *
from tkinter import messagebox
from random import choice, shuffle
import pyperclip


def password_generator():
    """Generate a random, 20 character password.  Fill password into entry box."""
    characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                  'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
                  'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7',
                  '8', '9', '!', '#', '$', '%', '&', '(', ')', '*', '+']

    # Delete entry from box if generate button pressed more than once
    password_entry.delete(0, END)

    # Pick random characters from list
    char_list = [choice(characters) for _ in range(20)]

    # Shuffle order of char_list
    shuffle(char_list)

    # Add characters in list to string
    pass_string = "".join(char_list)

    # Put generated password into entry field
    password_entry.insert(0, pass_string)


def save_record():
    """Pull data from entry boxes and save to file.  Copy password to clipboard.  Clear entry boxes after saving."""
    # Gather data and put into entry string
    delimiter = " | "
    site = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    entry = f"{site}{delimiter}{username}{delimiter}{password}\n"

    # Verify all fields have been filled out
    if len(site) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showwarning(title="Oops", message="Please fill in all fields.")
    else:
        # Ask user to confirm saving record
        is_ok = messagebox.askyesno(title=site, message=f"Email: {username}\nPassword: {password}\n"
                                                        f"Please confirm you want to add this record.")
        if is_ok:
            # Write entry to file
            with open("not_passwords.txt", "a") as record:
                record.write(entry)

            # Copy password to clipboard
            pyperclip.copy(password)

            # Delete data from site and password entries
            website_entry.delete(0, END)
            password_entry.delete(0, END)

            # Reset cursor to website entry
            website_entry.focus()


# Window Setup
window = Tk()
window.title("MyPass Password Manager")
window.config(padx=50, pady=50)

# Logo Setup
canvas = Canvas(width=200, height=200, highlightthickness=0)
lock_logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_logo)
canvas.grid(column=1, row=0)

# Website Label and Entry
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
website_entry = Entry(width=47)
website_entry.focus()  # Start with cursor in website_box
website_entry.grid(column=1, row=1, columnspan=2)

# Email/Username Label and Entry
username_label = Label(text="Email/Username:")
username_label.grid(column=0, row=2)
username_entry = Entry(width=47)
username_entry.insert(0, "username@email.com")  # Autofill email address
username_entry.grid(column=1, row=2, columnspan=2)

# Password Label, Entry, Generate Password Button
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)
password_entry = Entry(width=28)
password_entry.grid(column=1, row=3)
password_button = Button(text="Generate Password", command=password_generator, width=15)
password_button.grid(column=2, row=3)

# Add Record Button
add_button = Button(text="Add Record", command=save_record, width=58)
add_button.grid(column=0, row=4, columnspan=3)

window.mainloop()
