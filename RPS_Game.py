import tkinter as tk
from tkinter import PhotoImage
from tkinter import messagebox
import random

# Define the GUI window
root = tk.Tk()
root.title("Rock, Paper, Scissors")
root.geometry("400x400")

# Load images
rock_img = PhotoImage(file="rock.png")
paper_img = PhotoImage(file="paper.png")
scissors_img = PhotoImage(file="scissors.png")

# Function to play the game
def play_game(user_choice):
    computer_choice = random.choice(["rock", "paper", "scissors"])
    
    result = ""
    if user_choice == computer_choice:
        result = "It's a tie!"
    elif user_choice == "rock":
        if computer_choice == "paper":
            result = "You lost! Computer chose paper."
        else:
            result = "You won! Computer chose scissors."
    elif user_choice == "paper":
        if computer_choice == "scissors":
            result = "You lost! Computer chose scissors."
        else:
            result = "You won! Computer chose rock."
    else:
        if computer_choice == "rock":
            result = "You lost! Computer chose rock."
        else:
            result = "You won! Computer chose paper."
    
    messagebox.showinfo("Result", result)

# Rock button
rock_btn = tk.Button(root, image=rock_img, command=lambda: play_game("rock"))
rock_btn.pack(pady=10)
print("Rock")

# Paper button
paper_btn = tk.Button(root, image=paper_img, command=lambda: play_game("paper"))
paper_btn.pack(pady=10)
print("paper")

# Scissors button
scissors_btn = tk.Button(root, image=scissors_img, command=lambda: play_game("scissors"))
scissors_btn.pack(pady=10)
print("scissors")


# Start GUI event loop
root.mainloop()
