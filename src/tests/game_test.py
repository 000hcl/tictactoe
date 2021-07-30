import unittest
from ..board import Board

class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = Board(3)
    
    def test_board_is_correct_size(self):
        self.assertEqual(9, len(self.board.board))
    
    def test_check_tie_returns_true_when_board_is_full(self):
        board = ["X","X","O",
        "O","O","X",
        "X","X","O"]

        result = self.board.check_tie(board)
        self.assertTrue(result)
    
    def test_check_tie_returns_false_when_empty_spaces_exist(self):
        board = [None,"X","O",
        "O","O","X",
        "X","X","O"]

        result = self.board.check_tie(board)
        self.assertFalse(result)

    def test_check_verticals_returns_x_when_there_is_a_vertical_line_of_xs(self):
        board = ["X","O","O",
        "X","O","X",
        "X","X","O"]

        result = self.board.check_verticals(3, board)
        self.assertEqual("X", result)
    
    def test_check_verticals_returns_o_when_there_is_a_vertical_line_of_os(self):
        board = ["X","O","O",
        "X",None,"O",
        "O","X","O"]

        result = self.board.check_verticals(3, board)
        self.assertEqual("O", result)
    
    def test_check_verticals_returns_none_when_there_are_no_vertical_matches(self):
        board = ["X",None,"O",
        "O","O","X",
        "X","X","O"]

        result = self.board.check_verticals(3, board)
        self.assertEqual(None, result)
    
    def test_check_horizontals_returns_none_if_no_horizontal_matches_are_found(self):
        board = ["X",None,"O",
        "O","O","X",
        "X","X","O"]

        result = self.board.check_horizontal(3, board)
        self.assertEqual(None, result)
    
    def test_check_horizontal_returns_o_when_there_is_a_horizontal_line_of_os(self):
        board = ["O","O","O",
        "X","X",None,
        "X","O","X"]

        result = self.board.check_horizontal(3, board)
        self.assertEqual("O", result)
    
    def test_check_horizontal_returns_x_when_there_is_a_horizontal_line_of_xs(self):
        board = ["O",None,"O",
        "X","X","X",
        "X","O","X"]

        result = self.board.check_horizontal(3, board)
        self.assertEqual("X", result)
    
    def test_check_diagonal_rd_finds_diagonal_x(self):
        board = ["X","O",None,
        "O","X",None,
        "O","O","X"]

        result = self.board.check_diagonal_rd(3, board)
        self.assertEqual("X", result)
    
    def test_check_diagonal_rd_finds_diagonal_o(self):
        board = ["O","O",None,
        "X","O",None,
        "X","X","O"]

        result = self.board.check_diagonal_rd(3, board)
        self.assertEqual("O", result)
    
    def test_check_diagonal_rd_returns_none_when_there_are_no_diagonal_right_down_matches(self):
        board = [None, "O", "X",
        "O","X","O",
        "X",None,"O"]

        result = self.board.check_diagonal_rd(3, board)
        self.assertEqual(None, result)
    
    def test_check_diagonal_ld_finds_diagonal_x(self):
        board = [None, "O", "X",
        "O","X","O",
        "X",None,"O"]

        result = self.board.check_diagonal_ld(3, board)
        self.assertEqual("X", result)
    
    def test_check_diagonal_ld_finds_diagonal_o(self):
        board = [None, "O", "O",
        "X","O","X",
        "O",None,"X"]

        result = self.board.check_diagonal_ld(3, board)
        self.assertEqual("O", result)
    
    def test_check_diagonal_ld_returns_none_when_there_are_no_diagonal_left_down_matches(self):
        board = board = ["O","O",None,
        "X","O",None,
        "X","X","O"]

        result = self.board.check_diagonal_ld(3, board)
        self.assertEqual(None, result)