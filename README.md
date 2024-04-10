# Tic Tac Toe Game

This is a simple implementation of the classic Tic Tac Toe game using Python's Tkinter library for the GUI.

## Introduction

Tic Tac Toe is a two-player game where each player takes turns marking spaces in a 3x3 grid. The player who succeeds in placing three of their marks in a horizontal, vertical, or diagonal row wins the game.

## Algorithm Explanation

The game algorithm consists of several key functions that handle different aspects of gameplay. Let's break down each function and its role:

### 1. `check_win(board, player)`

This function checks if the given player has won the game by examining all possible winning combinations on the board. It iterates through each winning combination (rows, columns, and diagonals) and checks if all symbols in that combination belong to the specified player.

### 2. `check_tie(board)`

This function determines if the game has ended in a tie by checking if there are any empty spaces left on the board. If there are no empty spaces and no player has won, the game is declared a tie.

### 3. `get_available_moves(board)`

This function returns a list of available moves (indices of empty spaces) on the board. It iterates over the board and identifies all indices where the symbol is empty (denoted by a space character).

### 4. `ai_move(board)`

The AI strategy for making a move is implemented in this function. It follows these steps:
- First, it attempts to find a move that would result in an immediate win for the AI. It iterates through all available moves, temporarily placing an AI symbol in each empty space and checking if it leads to a win. If such a move is found, the function returns the index of that move.
- If no winning move is found, the function checks if the player is about to win in the next move. It does this by simulating the player's potential move for each available space and checking if it results in a win for the player. If such a move is found, the function blocks it by returning the index of that move with an AI symbol.
- If neither winning nor blocking moves are found, the function randomly selects an available move and returns its index.

### 5. `player_move(button, board)`

This function handles the player's move when they click on a button in the GUI. It first determines the index of the button clicked and checks if the corresponding space on the board is empty. If the space is empty, it updates the board with the player's symbol (O), disables the clicked button, and checks for a win or tie. If the game continues, the function triggers the AI's move by calling `ai_move` and updates the GUI accordingly.

### 6. `reset_game()`

This function resets the game by clearing the board and enabling all buttons in the GUI. It is called after a game ends (either by a win or tie) to prepare for a new game.

## Code Explanation

The Python code `main.py` implements the game logic and GUI using the Tkinter library. Here's a breakdown of the code:

1. **Imports:** Import the necessary libraries - Tkinter for GUI, messagebox for displaying messages, and random for AI move selection.

2. **Function Definitions:** Define the functions described above - `check_win`, `check_tie`, `get_available_moves`, `ai_move`, `player_move`, and `reset_game`.

3. **Initialize GUI:** Create a Tkinter window (`Tk()`) and set its title to "Tic Tac Toe". Initialize the game board as a list of empty spaces.

4. **Create Buttons:** Create a 3x3 grid of buttons using Tkinter's `Button` widget. Each button corresponds to a cell in the Tic Tac Toe grid. Bind the `player_move` function to each button so that it is triggered when the button is clicked.

5. **Mainloop:** Start the Tkinter event loop (`mainloop()`) to run the GUI application.

## Usage

To play the game:

1. Run the Python script `main.py`.
2. Click on the empty spaces in the GUI to make your move.
3. The game will alternate between player and AI moves.
4. The game ends when either player wins or it's a tie. Click "OK" on the message box to start a new game.

## TO-DO

- Implement more sophisticated AI algorithms for improved gameplay.
- Add options for customizing the game settings (e.g., board size, player names).
- Enhance the GUI with animations and visual effects to make the game more engaging.
- Implement a scoring system to keep track of wins, losses, and ties.
