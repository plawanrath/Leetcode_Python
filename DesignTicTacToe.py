"""
Assume the following rules are for the tic-tac-toe game on an n x n board between two players:

A move is guaranteed to be valid and is placed on an empty block.
Once a winning condition is reached, no more moves are allowed.
A player who succeeds in placing n of their marks in a horizontal, vertical, or diagonal row wins the game.
Implement the TicTacToe class:

TicTacToe(int n) Initializes the object the size of the board n.
int move(int row, int col, int player) Indicates that the player with id player plays at the cell (row, col) 
of the board. The move is guaranteed to be a valid move.


Idea:
The first player that makes n marks horizontally, vertically, or diagonally, wins the game.

The brute force approach to solve this problem is to iterate over the entire board of size n * n and 
check if the current player has marked any row, column, diagonal or anti-diagonal.

This approach is exhaustive and requires O(n^2) time for every move.

- There are only n (rows) + n (cols) + 2 (diagonals) ways to win the game
- So use a list to record the occurance
- For player 1, +1; for player 2, -1, verify the value after each call to determine the winner

Time COmplexity: O(1) - Because at every move we only mark a particular row/column
Space: O(n): row array, column array and 2 diagonals
"""
class TicTacToe:

    def __init__(self, n: int):
        self.n = n
        self.row = [0] * n # row
        self.col = [0] * n # col
        self.dia = [0] * 2 # diagonals

    def move(self, row: int, col: int, player: int) -> int:
        if player == 1:
            self.row[row] += 1
            self.col[col] += 1
            if row == col: 
                self.dia[0] += 1
            if row + col == self.n-1: 
                self.dia[1] += 1
            if self.row[row] == self.n or self.col[col] == self.n or self.dia[0] == self.n or self.dia[1] == self.n: 
                return 1
        else:     
            self.row[row] -= 1
            self.col[col] -= 1
            if row == col: 
                self.dia[0] -= 1
            if row + col == self.n-1: 
                self.dia[1] -= 1
            if self.row[row] == -self.n or self.col[col] == -self.n or self.dia[0] == -self.n or self.dia[1] == -self.n: 
                return 2
        return 0
