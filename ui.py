from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score = Label(text=f"Score: 0")
        self.score.config(bg=THEME_COLOR, foreground="white", padx=20, pady=20)
        self.score.grid(row=0, column=1)

        self.canvas = Canvas(width=400, height=350)
        # self.canvas.config(width=300, height=250)

        self.question_text = self.canvas.create_text(200, 175, text="question", font=('Arial', 20, 'italic'), width=380)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.right_image = PhotoImage(file="images/true.png")
        self.right = Button(image=self.right_image, highlightthickness=0, command=self.right_button_pressed)
        self.right.grid(row=2, column=0, pady=20, padx=20)

        self.wrong_image = PhotoImage(file="images/false.png")
        self.wrong = Button(image=self.wrong_image, highlightthickness=0, command=self.wrong_button_pressed)
        self.wrong.grid(row=2, column=1, pady=20, padx=20)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.canvas.config(bg="white")
            self.score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the Quiz")
            self.right.config(state="disabled")
            self.wrong.config(state="disabled")


    def right_button_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.right_or_wrong(is_right)

    def wrong_button_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.right_or_wrong(is_right)

    def right_or_wrong(self, true_or_false):
        if (true_or_false):
            self.canvas.config(bg="green", highlightthickness=0)
        else:
            self.canvas.config(bg="red", highlightthickness=0)

        self.window.after(1000, self.get_next_question)



