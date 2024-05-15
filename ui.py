THEME_COLOR = "#375362"

import tkinter as tk  ##Or from tkinter import *
from quiz_brain import QuizBrain


class QuizInterface:
    def __init__(self, quiz_brain:QuizBrain): ##input datatype: a QuizBrain obj -- need to pass in a QuizBrain object of QuizBrain-> So things in QuizBrain can be used here
        self.quiz = quiz_brain

        self.window = tk.Tk()
        self.window.title('My Quizzler')
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = tk.Canvas(height=250, width=300)
        self.canvas.config(highlightthickness=0, bg='white')
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=270,
            text=f'Let\'s Start!!',
            font=('Arial', 18, 'italic'),
            fill=THEME_COLOR)
        self.canvas.grid(column=0, row=1, columnspan=2,pady=50)


        self.score_label = tk.Label(text=f'Score=0', font=('Arial'), bg=THEME_COLOR, fg='white')
        self.score_label.grid(column=1, row=0)


        true_image = tk.PhotoImage(file='images/true.png')
        false_image = tk.PhotoImage(file='images/false.png')
        self.button_tick = tk.Button(image=true_image,highlightthickness=0, borderwidth=0, command=self.click_button_true)
        self.button_cross = tk.Button(image=false_image, highlightthickness=0, borderwidth=0, command=self.click_button_false)


        self.button_tick.grid(column=0, row=2)
        self.button_cross.grid(column=1, row=2)


        #----- RUN
        self.flip_timer = self.window.after(1000, self.get_next_question)



        #-----LOOP
        self.window.mainloop()

    def get_next_question(self):
        '''Use functions in quiz_brain by using the QuickBrain object, to get hold of question text'''
        self.canvas.config(bg='white')

        if self.quiz.still_has_questions():
            q_text= self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text=f"Your final score is: {self.quiz.score}/{self.quiz.question_number}")
            ## prevent the buttons from activated
            self.button_tick.config(state='disabled')
            self.button_cross.config(state='disabled')


    def click_button_true(self):
        user_answer = 'true'
        result = self.quiz.check_answer(user_answer)
        self.change_bg(result)


    def click_button_false(self):
        user_answer = 'false'
        result = self.quiz.check_answer(user_answer)
        self.change_bg(result)



    def change_bg(self, result):
        if result == True:
            self.canvas.config(bg='green')
            self.score_label.config(text=f'Score={self.quiz.score}')
        else:
            self.canvas.config(bg='red')

        # 1s后：go to the next question
        self.window.after_cancel(self.flip_timer) ##取消记时; 这里好像时间很短不用取消
        flip_timer = self.window.after(1000, self.get_next_question)



