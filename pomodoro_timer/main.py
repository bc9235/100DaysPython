from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

timer = None
reps = 0
check_text = ""


def reset_page():
    """Reset reps, timer, welcome text, and check marks."""
    global timer
    global reps
    reps = 0

    # Stop timer and reset timer text
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")

    # Reset check marks and welcome label
    check_marks.config(text="", bg=YELLOW)
    welcome_label.config(text="Welcome!")


def start_timer():
    """Determine how much time to put on the clock and start timer."""
    global reps
    reps += 1

    # Convert times into seconds
    work_seconds = WORK_MIN * 60
    short_break_seconds = SHORT_BREAK_MIN * 60
    long_break_seconds = LONG_BREAK_MIN * 60

    # Determine which timer runs based on how many reps have been completed
    if reps % 2 != 0:
        welcome_label.config(text="Work", fg=GREEN)
        countdown(work_seconds)
    elif reps % 8 == 0:
        welcome_label.config(text="Break!", fg=RED)
        countdown(long_break_seconds)
    else:
        welcome_label.config(text="Break!", fg=PINK)
        countdown(short_break_seconds)


def countdown(count):
    """Countdown from # minutes, add check mark for each work set done."""
    global timer
    global reps
    global check_text
    # Convert seconds to minutes
    count_minutes = math.floor(count / 60)
    # Remaining seconds
    count_seconds = count % 60
    if count_seconds < 10:
        count_seconds = f"0{count_seconds}"
    # Change timer_text to countdown numbers
    canvas.itemconfig(timer_text, text=f"{count_minutes}:{count_seconds}")
    if count > 0:
        timer = window.after(1000, countdown, count - 1)
    else:
        if reps % 2 != 0:
            check_text += "✅"
            check_marks.config(text=check_text, fg=GREEN, bg=YELLOW)
        start_timer()


# Window Setup
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Canvas Setup
# Background Image and Timer Text
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato)
timer_text = canvas.create_text(100, 135, text="00:00", fill="white", font=(FONT_NAME, 34, "bold"))
canvas.grid(column=1, row=1)

# Buttons
start = Button(text="Start", highlightthickness=0, command=start_timer)
start.grid(column=0, row=2)

reset = Button(text="Reset", highlightthickness=0, command=reset_page)
reset.grid(column=2, row=2)

# Labels
welcome_label = Label(text="Welcome!", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40, "bold"))
welcome_label.grid(column=1, row=0)

check_marks = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 14, "bold"))
check_marks.grid(column=1, row=3)

window.mainloop()
