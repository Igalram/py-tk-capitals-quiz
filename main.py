import tkinter as tk
from tkinter import font
import random
from capitals import populatequest
import pygame

import os
print("Current working directory:", os.getcwd())

class CapitalsQuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Capitals Quiz")


        # initialize sounds
        pygame.mixer.init()

        #self.correctsound=pygame.mixer.Sound("correct.wav")
        #self.incorrectsound=pygame.mixer.Sound("incorrect.wav")
          
        # Create a frame for better layout management
        self.frame = tk.Frame(root)
        self.frame.pack(pady=20, padx=20)

         # create Question Label
        self.question_label = tk.Label(self.frame, text="What is the capital of:", font=("Arial", 16))
        self.question_label.grid(row=0, column=0, columnspan=2, pady=10)

        # create Country label
        self.country_label = tk.Label(self.frame, text="", font=("Arial", 20, "bold"))
        self.country_label.config(text="")
        self.country_label = tk.Label(self.frame, text="", font=("Arial", 20, "bold"))
        self.country_label.grid(row=1, column=0, columnspan=2, pady=10)

         # Result Message Label
        
        self.result_label = tk.Label(self.frame, text="", font=("Arial", 14))
        self.result_label.grid(row=2, column=0, columnspan=2, pady=10)
        self.result_label.config(text="")
        
        self.load_question()
       

    def load_question(self):
        
        # Populate a new question list
        self.quizlist = populatequest()
        
       
        rnd=random.randint(0,3)
        self.correct_answer=self.quizlist[rnd]['city']
        self.country_label.config(text=f"{self.quizlist[rnd]['country']}") 
        

        # Result Message Label
        
        
        self.result_label.config(text="")
        
        # Answer Buttons
        self.buttons = []
        for i in range(4):
            button = tk.Button(self.frame, text=f"{self.quizlist[i]['city']}", width=20, font=("Arial", 14), command=lambda idx=i: self.check_answer(idx))
            button.grid(row=3 + i // 2, column=i % 2, padx=10, pady=10)
            self.buttons.append(button)

    def check_answer(self, idx):
        # This function will be updated later with actual quiz logic
        selected_option = self.buttons[idx].cget("text")
        if selected_option==self.correct_answer:
            self.result_label.config(text="HURRAA!!! Your answer is correct!")
            #self.play_sound(self.correctsound)
        else:
            self.result_label.config(text=f"Wrong, the right answer was {self.correct_answer}, better luck next time!")
            #self.play_sound(self.incorrectsound)
        self.root.after(2000, self.load_question)



if __name__ == "__main__":
    root = tk.Tk()
    app = CapitalsQuizApp(root)
    root.mainloop()
