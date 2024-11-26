import unittest
import numpy as np
from Board import Board


class TestBoard(unittest.TestCase):

    def test_drop_piece(self):
        c4 = Board()
        self.assertTrue(c4.drop_piece(0))
        self.assertTrue(c4.drop_piece(0))
        self.assertTrue(c4.drop_piece(0))
        self.assertTrue(c4.drop_piece(0))
        self.assertTrue(c4.drop_piece(0))
        self.assertTrue(c4.drop_piece(0))
        self.assertFalse(c4.drop_piece(0))
        self.assertFalse(c4.drop_piece(0))
        expected_board = np.zeros((6, 7), dtype=np.int8)
        expected_board[:, 0] = [1, 2, 1, 2, 1, 2]
        np.testing.assert_array_equal(c4.board, expected_board)