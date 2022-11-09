class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.score = 0
        self.question_list = question_list

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, u_answer, q_answer):
        if u_answer.lower() == q_answer.lower():
            self.score += 1
            print(f"You got it right!\nYour score: {self.score}/{self.question_number}\n")
        else:
            print(f"That's wrong.\nYour score: {self.score}/{self.question_number}\n")

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        u_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False)? ")
        self.check_answer(u_answer, current_question.answer)
