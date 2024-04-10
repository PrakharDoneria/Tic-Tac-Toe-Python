import tkinter as tk
from tkinter import messagebox
import random

def check_win(board, player):
    return ((board[0] == board[1] == board[2] == player) or
            (board[3] == board[4] == board[5] == player) or
            (board[6] == board[7] == board[8] == player) or
            (board[0] == board[3] == board[6] == player) or
            (board[1] == board[4] == board[7] == player) or
            (board[2] == board[5] == board[8] == player) or
            (board[0] == board[4] == board[8] == player) or
            (board[2] == board[4] == board[6] == player))

def check_tie(board):
    return " " not in board

def get_available_moves(board):
    return [i for i, x in enumerate(board) if x == " "]

def ai_move(board):
    for move in get_available_moves(board):
        board[move] = "X"
        if check_win(board, "X"):
            return move
        board[move] = " "

    for move in get_available_moves(board):
        board[move] = "O"
        if check_win(board, "O"):
            board[move] = "X"
            return move
        board[move] = " "

    return random.choice(get_available_moves(board))

def player_move(button, board):
    index = buttons.index(button)
    if board[index] == " ":
        board[index] = "O"
        button.config(text="O", state="disabled")
        if check_win(board, "O"):
            messagebox.showinfo("Tic Tac Toe", "You win!")
            reset_game()
        elif check_tie(board):
            messagebox.showinfo("Tic Tac Toe", "It's a tie!")
            reset_game()
        else:
            ai_index = ai_move(board)
            buttons[ai_index].config(text="X", state="disabled")
            if check_win(board, "X"):
                messagebox.showinfo("Tic Tac Toe", "AI wins!")
                reset_game()
            elif check_tie(board):
                messagebox.showinfo("Tic Tac Toe", "It's a tie!")
                reset_game()

def reset_game():
    for button in buttons:
        button.config(text=" ", state="normal")
    global board
    board = [" " for _ in range(9)]

root = tk.Tk()
root.title("Tic Tac Toe")

board = [" " for _ in range(9)]

buttons = []
for i in range(9):
    button = tk.Button(root, text=" ", font=("Helvetica", 20), width=3, height=1,
                       command=lambda i=i: player_move(buttons[i], board))
    button.grid(row=i // 3, column=i % 3)
    buttons.append(button)

root.mainloop()
