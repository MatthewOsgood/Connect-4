import numpy as np


class Board:
    MAX = 1
    MIN = 2
    def __init__(self, width=7, height=6):
        self.width = width
        self.height = height
        self.board = np.zeros((height, width), dtype=np.int8)
        self.moves = 0
        # stores the height of the top piece in each column
        self.heights = np.zeros(width, dtype=np.int8)
    
    def copy(self, board):
        b = Board()
        b.width, b.height = self.width, self.height
        b.board = self.board.copy()
        b.moves = self.moves
        b.height = self.heights.copy()
        return b

    def __str__(self):
        s = ""
        for row in range(self.height - 1, -1, -1):
            for col in range(self.width):
                s += str(self.board[row][col]) + " "
            s += "\n"
        s += "-" * (self.width * 2 - 1) + "\n"
        for col in range(self.width):
            s += str(col) + " "
        s += "\n"
        for h in self.heights:
            s += str(h) + " "
        s += "h"
        return s

    def current_player(self):
        """
        return the current player
        """
        return self.moves % 2 + 1
    
    def can_play(self, col) -> bool:
        """
        return True if the column col is not full 
        """
        return self.heights[col] < self.height

    def drop_piece(self, col):
        """
        drop a piece in column col. The piece will be placed in the lowest available row in that column
        assumes that the column is not full
        :param col: the column to place the piece ranges from 0 to width - 1
        """
        self.board[self.heights[col]][col] = self.current_player()
        self.heights[col] += 1
        self.moves += 1

    def is_full(self) -> bool:
        """
        return True if the board is full. This means that the game is a draw
        :return:
        """
        return self.moves == self.width * self.height

    def is_winning_move(self, col) -> bool:
        """
        return true if the current player playing in column col will result in a terminal state
        """
        row = self.heights[col]
        # check vertical
        if (row >= 3 and 
            self.board[row - 1][col] == self.current_player() and
            self.board[row - 2][col] == self.current_player() and
            self.board[row - 3][col] == self.current_player()):
            return True
        # check horizontal
        # for c in range(max(0, col - 3), min(self.width - 3, col)):
        #     if (self.board[row][c] == self.current_player and
        #             self.board[row][c + 1] == self.current_player and
        #             self.board[row][c + 2] == self.current_player and
        #             self.board[row][c + 3] == self.current_player):
        #         return True
        for dy in [-1, 0, 1]: # check negative slope diagonal, horizontal, positive slope diagonal
            nb = 0
            for dx in [-1, 1]: # check left and right
                x = col + dx
                y = row + dx * dy
                while 0 <= x < self.width and 0 <= y < self.height and self.board[y][x] == self.current_player():
                    nb += 1
                    x += dx
                    y += dx * dy
            if nb >= 3:
                return True
        return False
    
    def play(self, moves):
        for move in moves:
            if self.can_play(int(move)):
                self.drop_piece(int(move))
            else:
                print(f"Player {self.current_player()} failed to play in column {move} on turn {self.moves}")
                print(self)
                return


if __name__ == "__main__":
    c4 = Board()
    print(c4)