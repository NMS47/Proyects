from tkinter import *
from quiz_brain import QuizBrain
from time import time
THEME_COLOR = "#375362"


class QuizzGUI:

    def __init__(self, quiz_brain: QuizBrain):
        self.window = Tk()
        self.window.title('Quizz Game')
        self.window.config(bg=THEME_COLOR)
        self.quiz = quiz_brain

        self.canva = Canvas(width=300, height=250,)
        self.canva.grid(row=1, column=0, columnspan=2, padx=20, pady=20)

        self.question = self.canva.create_text(150, 125, text='question', width=200, font=('Arial', 20, 'italic'))
        self.score = Label(text="Score: 0",
                           font=('Arial', 14,),
                           bg=THEME_COLOR, fg='white',
                           padx=20, pady=20)
        self.score.grid(row=0, column=1)

        img_right = PhotoImage(file='images/true.png')
        self.true_button = Button(self.window, image=img_right, pady=20, highlightthickness=0,
                                  bg=THEME_COLOR, command=self.ans_true)
        self.true_button.grid(row=2, column=1)
        img_wrong = PhotoImage(file='images/false.png')
        self.wrong_button = Button(self.window, image=img_wrong, pady=20, highlightthickness=0,
                                  bg=THEME_COLOR, command=self.ans_false)
        self.wrong_button.grid(row=2, column=0)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        data = self.quiz.next_question()
        self.canva.itemconfig(self.question, text=data)

    def ans_true(self):
        user_answer = 'True'
        current_score, is_correct = self.quiz.check_answer(user_answer)
        self.score.config(text=current_score)
        if not is_correct:
            self.canva.config(bg='red')
            self.window.after(2000, self.ans_feedback)
        else:
            self.canva.config(bg='green')
            self.window.after(2000, self.ans_feedback)

    def ans_false(self):
        user_answer = 'True'
        current_score, is_correct = self.quiz.check_answer(user_answer)
        self.score.config(text=current_score)
        if not is_correct:
            self.canva.config(bg='red')
            self.window.after(2000, self.ans_feedback)
        else:
            self.canva.config(bg='green')
            self.window.after(2000, self.ans_feedback)

    def ans_feedback(self):
        self.canva.config(bg='white')
        try:
            self.get_next_question()
        except IndexError:
            self.canva.itemconfig(self.question, text="Finished")
            self.true_button.config(state='disabled')
            self.wrong_button.config(state='disabled')

