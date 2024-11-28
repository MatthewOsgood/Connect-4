import unittest
import numpy as np
from Board import Board
from Solver import solve


class TestBoard(unittest.TestCase):

    def test_drop_piece(self):
        c4 = Board()
        c4.drop_piece(0)
        self.assertEqual(c4.board[1][0], Board.MAX)
        c4.drop_piece(0)
        self.assertEqual(c4.board[2][0], Board.MIN)
        c4.drop_piece(0)
        self.assertEqual(c4.board[1][0], Board.MAX)
        c4.drop_piece(0)
        self.assertEqual(c4.board[2][0], Board.MIN)
        c4.drop_piece(0)
        self.assertEqual(c4.board[1][0], Board.MAX)
        c4.drop_piece(0)
        self.assertEqual(c4.board[2][0])
        expected_board = np.zeros((6, 7), dtype=np.int8)
        expected_board[:, 0] = [1, 2, 1, 2, 1, 2]
        np.testing.assert_array_equal(c4.board, expected_board)
        
    def test_current_player(self):
        c4 = Board()
        self.assertEqual(c4.current_player(), Board.MAX)
        c4.drop_piece(0)
        self.assertEqual(c4.current_player(), Board.MIN)
        c4.drop_piece(0)
        self.assertEqual(c4.current_player(), Board.MAX)
        
    def test_can_play(self):
        c4 = Board()
        self.assertTrue(c4.can_play(0))
        self.assertTrue(c4.can_play(c4.width - 1))
        for i in range(c4.height):
            self.assertTrue(c4.can_play(0))
            c4.drop_piece(0)
        self.assertFalse(c4.can_play(0))
    
    def test_is_full(self):
        c4 = Board()
        self.assertFalse(c4.is_full())
        for i in range(c4.width):
            for j in range(c4.height):
                if c4.can_play(i):
                    c4.drop_piece(i)
        self.assertTrue(c4.is_full())
        
    def test_is_winning_move_vertical(self):
        c4 = Board()
        self.assertFalse(c4.is_winning_move(0))
        c4.play("010101")
        self.assertTrue(c4.is_winning_move(0))
        self.assertFalse(c4.is_winning_move(1))

    def test_is_winning_move_horizontal(self):
        c4 = Board()
        c4.play("001122")
        self.assertTrue(c4.is_winning_move(3))
        self.assertFalse(c4.is_winning_move(4))
    
    def test_is_winning_move_diagonal_positive(self):
        c4 = Board()
        """
        0 0 0 0 0 0 0
        0 0 0 0 0 0 0
        0 0 0 0 0 0 0
        0 0 1 2 0 0 0
        0 1 1 2 0 0 0
        1 2 2 2 1 0 0
        """
        c4.play("0112232343")
        self.assertTrue(c4.is_winning_move(3))
        
    def test_is_winning_move_diagonal_negative(self):
        """
        0 0 0 1 0 0 0
        0 0 0 1 1 0 0
        0 0 0 2 1 1 0
        0 0 0 1 2 2 1
        0 0 0 2 1 1 2
        0 0 2 2 2 2 1
        """
        c4 = Board()
        c4.play("666555544443433330")
        self.assertTrue(c4.is_winning_move(3))
        
    def test_copy(self):
        c4 = Board()
        c4.drop_piece(0)
        c4.drop_piece(1)
        c4.drop_piece(2)
        c4.drop_piece(3)
        c4.drop_piece(4)
        c4.drop_piece(5)
        c4.drop_piece(6)
        c4.drop_piece(0)
        c4.drop_piece(0)
        c4.drop_piece(0)
        c4_copy = c4.copy()
        self.assertEqual(c4.moves, c4_copy.moves)
        np.testing.assert_array_equal(c4.board, c4_copy.board)
        np.testing.assert_array_equal(c4.heights, c4_copy.heights)
        c4.drop_piece(0)
        self.assertNotEqual(c4.moves, c4_copy.moves)
        self.assertNotEqual(c4.board.tolist(), c4_copy.board.tolist())
        self.assertNotEqual(c4.heights.tolist(), c4_copy.heights.tolist())
        
    def test_solve(self):
        c4 = Board()
        c4.play("001122")
        score, optimal_move = solve(c4)
        self.assertEqual(optimal_move, 3)
        print(score, optimal_move)