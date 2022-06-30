from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR)
        self.window.config(padx=20, pady=20)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.canvas.grid(row=1, column=0, columnspan=2, pady=30)

        self.question_text = self.canvas.create_text(150, 125, text="Question", font=("Arial", 20, "italic"), width=280)

        self.score = Label(text="Score: 0", bg=THEME_COLOR, fg="white")
        self.score.grid(row=0, column=1)

        true_button_image = PhotoImage(file="images/true.png")
        self.true_answer = Button(image=true_button_image, borderwidth=0, highlightthickness=0, command=self.true_button)
        self.true_answer.grid(row=2, column=0)

        false_button_image = PhotoImage(file="images/false.png")
        self.false_answer = Button(image=false_button_image, borderwidth=0, highlightthickness=0, command=self.false_button)
        self.false_answer.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="The quiz is end")
            self.true_answer.config(state="disabled")
            self.false_answer.config(state="disabled")

    def true_button(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_button(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)



