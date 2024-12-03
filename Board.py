import numpy as np
from termcolor import colored


class Board:
    MAX = np.int8(1)
    MIN = np.int8(2)
    WIDTH = 7
    HEIGHT = 6
    SEARCH_ORDER = (3, 2, 4, 1, 5, 0, 6)
    HEURISTIC_TABLE = np.array(((3, 4, 5,  7,  5,  4, 3),
	                            (4, 6, 8,  10, 8,  6, 4),
	                            (5, 8, 11, 13, 11, 8, 5),
	                            (5, 8, 11, 13, 11, 8, 5),
	                            (4, 6, 8,  10, 8,  6, 4),
	                            (3, 4, 5,  7,  5,  4, 3))) / 6 # scale down to fit with minimax score based on how many moves required to win
    MIN_SCORE = -(WIDTH * HEIGHT // 2) + 3
    
    
    def __init__(self):
        self.board = np.zeros((self.HEIGHT, self.WIDTH), dtype=np.int8)
        self.moves = 0
        # stores the height of the top piece in each column
        self.heights = np.zeros(self.WIDTH, dtype=np.int8)
    
    def copy(self):
        """
        :return: a deep copy of this board
        """
        b = Board()
        b.board = self.board.copy()
        b.moves = self.moves
        b.heights = self.heights.copy()
        return b

    def __str__(self):
        s = ""
        for row in range(self.HEIGHT - 1, -1, -1):
            for col in range(self.WIDTH):
                if self.board[row][col] == 0:
                    s += "0"
                elif self.board[row][col] == Board.MAX:
                    s += colored('1', "red")
                else:
                    s += colored('2', "yellow")
                s += " "
            s += "\n"
        s += "-" * (self.WIDTH * 2 - 1) + "\n"
        for col in range(1, self.WIDTH + 1):
            s += str(col) + " "
        return s

    def current_player(self):
        """
        :return: the current player
        """
        return self.moves % 2 + 1
    
    def can_play(self, col) -> bool:
        """
        :return: True if the column col is not full
        """
        return self.heights[col] < self.HEIGHT

    def drop_piece(self, col):
        """
        drop a piece in column col. The piece will be placed in the lowest available row in that column
        assumes that the column is not full
        :param col: the column to place the piece ranges from 0 to 6
        """
        self.board[self.heights[col]][col] = self.current_player()
        self.heights[col] += 1
        self.moves += 1

    def is_full(self) -> bool:
        """
        return True if the board is full. This means that the game is a draw
        :return:
        """
        return self.moves == self.WIDTH * self.HEIGHT

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
        for dy in [-1, 0, 1]: # check negative slope diagonal, horizontal, positive slope diagonal
            nb = 0
            for dx in [-1, 1]: # check left and right
                x = col + dx
                y = row + dx * dy
                while 0 <= x < self.WIDTH and 0 <= y < self.HEIGHT and self.board[y][x] == self.current_player():
                    nb += 1
                    x += dx
                    y += dx * dy
            if nb >= 3:
                return True
        return False
    
    def play(self, moves):
        """
        play the moves in the string moves
        :param moves: a string of integers 
        :return: if the piece was played, and the result (0 for no change, -1 for min win, 1 for max win)
        """
        for move in moves:
            if self.can_play(int(move)):
                if self.is_winning_move(int(move)):
                    winner = self.current_player()
                    self.drop_piece(int(move))
                    return True, winner
                self.drop_piece(int(move))
            else:
                print(colored(f"Player {self.current_player()} failed to play in column {move} on turn {self.moves}", "red"))
                return False, 0
        return True, 0
            
    def heuristic_value(self) -> int:
        """
        calculates the heuristic value of this board for the current player
        """
        value = 0
        for row in range(self.HEIGHT):
            for col in range(self.WIDTH):
                if self.board[row][col] == self.current_player():
                    value += self.HEURISTIC_TABLE[row][col]
                else:
                    value -= self.HEURISTIC_TABLE[row][col]
        return value
