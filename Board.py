import numpy as np


class Board:
    MAX = 1
    MIN = 2
    def __init__(self, width=7, height=6):
        self.width = width
        self.height = height
        self.board = np.zeros((height, width), dtype=np.int8)
        self.moves = 0

    def __str__(self):
        s = ""
        for row in range(self.height - 1, -1, -1):
            for col in range(self.width):
                s += str(self.board[row][col]) + " "
            s += "\n"
        s += "-" * (self.width * 2 - 1) + "\n"
        for col in range(self.width):
            s += str(col) + " "
        return s

    def current_player(self):
        """
        return the current player
        """
        return self.moves % 2 + 1

    def drop_piece(self, col) -> bool:
        """
        drop a piece in column col. The piece will be placed in the lowest available row in that column
        :param col: the column to place the piece ranges from 0 to width - 1
        :return: True if the piece was successfully placed, False otherwise
        """
        for row in range(self.height):
            if self.board[row][col] == 0:
                self.board[row][col] = self.current_player()
                self.moves += 1
                return True # for bug testing
        return False

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
        # check vertical
        for row in range(self.height - 3):
            if self.board[row][col] == self.current_player and self.board[row + 1][col] == self.current_player and self.board[row + 2][col] == self.current_player and self.board[row + 3][col] == self.current_player:
                return True



if __name__ == "__main__":
    c4 = Board()
    print(c4)