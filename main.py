import tkinter as tk
from tkinter import messagebox

# Create an empty board
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

# Variable to track the current player (X or O)
current_player = "X"

# Create the main window
window = tk.Tk()
window.title("Tic-Tac-Toe")

# Function to handle a button click
def handle_click(row, col):
    global current_player

    # Check if the clicked button is already marked
    if board[row * 3 + col] != "-":
        messagebox.showinfo("Invalid Move", "That position is already marked!")
        return

    # Mark the button with the current player's symbol
    button = buttons[row][col]
    button.config(text=current_player, state=tk.DISABLED)

    # Update the board
    board[row * 3 + col] = current_player

    # Check if the game is over
    if check_winner(current_player):
        messagebox.showinfo("Game Over", "Player " + current_player + " wins!")
        window.quit()
        return
    elif check_tie():
        messagebox.showinfo("Game Over", "It's a tie!")
        window.quit()
        return

    # Switch to the other player
    current_player = "O" if current_player == "X" else "X"

# Function to check if any player has won
def check_winner(player):
    # Check rows
    for i in range(3):
        if board[i * 3] == board[i * 3 + 1] == board[i * 3 + 2] == player:
            return True
    # Check columns
    for i in range(3):
        if board[i] == board[i + 3] == board[i + 6] == player:
            return True
    # Check diagonals
    if board[0] == board[4] == board[8] == player:
        return True
    if board[2] == board[4] == board[6] == player:
        return True
    return False

# Function to check if the game is a tie
def check_tie():
    if "-" not in board:
        return True
    return False

# Create buttons for the board
buttons = []
for i in range(3):
    row = []
    for j in range(3):
        button = tk.Button(window, text="-", width=10, height=5,
                          command=lambda r=i, c=j: handle_click(r, c))
        button.grid(row=i, column=j)
        row.append(button)
    buttons.append(row)

# Start the main event loop
window.mainloop()
