from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        """Set up GUI"""
        self.quiz = quiz_brain

        # Set up Window
        self.window = Tk()
        self.window.title("Quiz Game")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        # Set up Scoreboard
        self.scoreboard = Label(text="Score: 0", fg="white", bg=THEME_COLOR, font=("Arial", 16, "normal"))
        self.scoreboard.grid(column=1, row=0)

        # Set up Canvas to display question
        self.canvas = Canvas(width=300, height=250, bg="white")
        # Set up Question Text
        self.text = self.canvas.create_text(150, 125, width=280, text="", font=FONT, fill=THEME_COLOR)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        # Set up Buttons
        true_image = PhotoImage(file="images/true.png")
        self.true = Button(image=true_image, command=self.click_true, bg=THEME_COLOR, highlightthickness=0)
        self.true.grid(column=1, row=2)

        false_image = PhotoImage(file="images/false.png")
        self.false = Button(image=false_image, command=self.click_false, bg=THEME_COLOR, highlightthickness=0)
        self.false.grid(column=0, row=2)

        # Display question
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        """Get next question from question bank, display on screen, update score."""
        self.canvas.config(bg="white")  # Change canvas to white
        if self.quiz.still_has_questions():
            self.scoreboard.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.text, text=q_text)
        else:
            self.canvas.itemconfig(self.text, text="You've reached the end of the quiz.")
            # Disable buttons if out of questions
            self.true.config(state="disabled")
            self.false.config(state="disabled")

    def click_true(self):
        """Check user guess."""
        is_right = self.quiz.check_answer(user_answer="True")
        self.give_feedback(is_right)

    def click_false(self):
        """Check user guess."""
        is_right = self.quiz.check_answer(user_answer="False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        """Change canvas color to indicate whether user guess is right or wrong."""
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        # After 1 second, call get_next_question
        self.window.after(1000, self.get_next_question)
