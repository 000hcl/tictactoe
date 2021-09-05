import unittest
from .. import board as b


class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = b.Board(3)
        self.big_board = b.Board(30)

    def test_board_is_correct_size(self):
        self.assertEqual(9, len(self.board.board))

    def test_check_tie_returns_true_when_board_is_full(self):
        board = ["X", "X", "O",
                 "O", "O", "X",
                 "X", "X", "O"]

        result = self.board.check_tie(board)
        self.assertTrue(result)

