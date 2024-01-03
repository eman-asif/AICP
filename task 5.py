import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.current_player = "X"

        # Create buttons for the Tic Tac Toe grid
        self.buttons = [[tk.Button(root, text="", font=('Helvetica', 24), width=5, height=2,
                                   command=lambda row=row, col=col: self.make_move(row, col))
                         for col in range(3)] for row in range(3)]

        # Place the buttons in the grid
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].grid(row=row, column=col)

    def make_move(self, row, col):
        button = self.buttons[row][col]
        if button["text"] == "":
            button["text"] = self.current_player
            if self.check_winner(row, col):
                messagebox.showinfo("Tic Tac Toe", f"Player {self.current_player} wins!")
                self.reset_board()
            elif self.check_draw():
                messagebox.showinfo("Tic Tac Toe", "It's a draw!")
                self.reset_board()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self, row, col):
        # Check the current row
        if all(self.buttons[row][i]["text"] == self.current_player for i in range(3)):
            return True
        # Check the current column
        if all(self.buttons[i][col]["text"] == self.current_player for i in range(3)):
            return True
        # Check the main diagonal
        if row == col and all(self.buttons[i][i]["text"] == self.current_player for i in range(3)):
            return True
        # Check the anti-diagonal
        if row + col == 2 and all(self.buttons[i][2 - i]["text"] == self.current_player for i in range(3)):
            return True
        return False

    def check_draw(self):
        return all(button["text"] != "" for row in self.buttons for button in row)

    def reset_board(self):
        for row in range(3):
            for col in range(3):
                self.buttons[row][col]["text"] = ""
        self.current_player = "X"


def main():
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
main()