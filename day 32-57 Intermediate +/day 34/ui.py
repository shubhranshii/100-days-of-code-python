from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score_label = Label(text="Score=0", bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.q_statement = self.canvas.create_text(150,
                                                   125,
                                                   width=280,
                                                   text="question statement",
                                                   font=("Arial", 20, "italic"), fill=THEME_COLOR)

        tick_img = PhotoImage(file="./images/true.png")
        self.tick_button = Button(image=tick_img, command=self.check_true)
        self.tick_button.grid(row=2, column=0)

        cross_img = PhotoImage(file="./images/false.png")
        self.cross_button = Button(image=cross_img, command=self.check_false)
        self.cross_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        self.score_label.config(text=f"Score={self.quiz.score}")
        if self.quiz.still_has_questions():
            self.button_enable()
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.q_statement, text=q_text)
        else:
            self.canvas.itemconfig(self.q_statement,
                                   text=f"Quiz Completed!\n Your score is {self.quiz.score}/10")
            self.score_label.config(text="")
            self.button_disable()


    def check_true(self):
        self.button_disable()
        self.give_feedback(self.quiz.check_answer("True"))


    def check_false(self):
        self.button_disable()
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)

    def button_enable(self):
        self.tick_button.config(state="normal")
        self.cross_button.config(state="normal")

    def button_disable(self):
        self.tick_button.config(state="disabled")
        self.cross_button.config(state="disabled")
