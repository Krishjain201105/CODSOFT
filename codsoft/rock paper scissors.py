import tkinter as tk
from tkinter import ttk,messagebox
import random

user_score = 0
computer_score = 0

def play_game(user_choice):
    global user_score, computer_score
    computer_choice = random.choice(["Rock", "Paper", "Scissors"])
    
    if user_choice == computer_choice:
        result = "Tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Scissors" and computer_choice == "Paper") or \
         (user_choice == "Paper" and computer_choice == "Rock"):
        result = "You win!"
        user_score += 1
    else:
        result = "You lose!"
        computer_score += 1

    result_label.config(text=f"You chose: {user_choice}\nComputer chose: {computer_choice}\nResult: {result}")
    score_label.config(text=f"Your Score: {user_score} | Computer Score: {computer_score}")

def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    score_label.config(text=f"Your Score: {user_score} | Computer's Score: {computer_score}")
    result_label.config(text="")


root = tk.Tk()
root.title("Rock Paper Scissors Game")

choice = tk.Label(root, text="Choose Rock, Paper, or Scissors:")
choice.pack(padx=10,pady=15)


rock_button = ttk.Button(root, text="Rock", command=lambda: play_game("Rock"), width=25)
rock_button.pack(padx=10,pady=15)

paper_button = ttk.Button(root, text="Paper", command=lambda: play_game("Paper"), width=25)
paper_button.pack(padx=10,pady=15)

scissors_button = ttk.Button(root, text="Scissors", command=lambda: play_game("Scissors"), width=25)
scissors_button.pack(padx=10,pady=15)


result_label = tk.Label(root, text="")
result_label.pack(padx=10,pady=15)

score_label = tk.Label(root, text=f"Your Score: {user_score} | Computer Score: {computer_score}")
score_label.pack(padx=10,pady=15)

reset_button = ttk.Button(root, text="Reset Scores", command=reset_game, width=15)
reset_button.pack(padx=10,pady=15)

root.mainloop()
