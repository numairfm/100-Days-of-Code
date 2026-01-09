import tkinter as tk
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizUi:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz_brain = quiz_brain
        self.finished: bool = False
        
        self.window = tk.Tk()
        self.window.minsize(450,600)
        self.window.maxsize(450,600)
        self.window.title("Quizler")
        self.window.config(padx=20, pady=20, background=THEME_COLOR)
        
        self.score_text = tk.Label(text="Score: 0", font=("Arial", 16, "normal"), background=THEME_COLOR)
        self.score_text.grid(row=0, column=1)
        
        self.canvas = tk.Canvas(width=410, height=340, background="#ffffff")
        self.question_text = self.canvas.create_text(205, 170, text="question", font=("Arial", 20, "italic"), width=370)
        self.canvas.grid(row=2, column=0, columnspan=2, pady=40)
        
        true_image = tk.PhotoImage(file="images/true.png")
        self.true_button = tk.Button(image=true_image, command=self.true_pressed)
        self.true_button.grid(row=3, column=0)
        
        false_image = tk.PhotoImage(file="images/false.png")
        self.false_button = tk.Button(image=false_image, command=self.false_pressed)
        self.false_button.grid(row=3, column=1)
        
        self.get_next_question()
        
        self.window.mainloop()
        
    def get_next_question(self):
        q_text = self.quiz_brain.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)
        
    def true_pressed(self):
        if not self.finished:
            old_score = self.quiz_brain.score
            
            self.quiz_brain.check_answer("True")
            self.score_text.config(text=f"Score: {self.quiz_brain.score}")
            
            if old_score == self.quiz_brain.score:
                self.canvas.config(background="#ff0000")
                self.window.after(1000, func=self.reset_canvas_color)
            else:
                self.canvas.config(background="#008000")
                self.window.after(1000, func=self.reset_canvas_color)
                
        if self.quiz_brain.still_has_questions():
            self.get_next_question()
        else:
            self.finished = True
            self.canvas.itemconfig(self.question_text, text=f"Final Score: {self.quiz_brain.score}/{self.quiz_brain.question_number}")
            
    def false_pressed(self):
        if not self.finished:
            old_score = self.quiz_brain.score
            
            self.quiz_brain.check_answer("False")
            self.score_text.config(text=f"Score: {self.quiz_brain.score}")
            
            if old_score == self.quiz_brain.score:
                self.canvas.config(background="#ff0000")
                self.window.after(1000, func=self.reset_canvas_color)
            else:
                self.canvas.config(background="#008000")
                self.window.after(1000, func=self.reset_canvas_color)
    
                
        if self.quiz_brain.still_has_questions():
            self.get_next_question()
        else:
            self.finished = True
    
    def reset_canvas_color(self):
        self.canvas.config(background="#ffffff")