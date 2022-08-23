import unittest

from .chessboard import Chessboard


class Queentest(unittest.TestCase):
    def test_empty_board(self):
        board = Chessboard()
        assert board.is_empty() is True

    # def test_draw_empty_board(self):
    #     board = Chessboard()
    #     with open("eight-queens/empty_board.txt", "r") as empty_board:
    #         assert board.print_board() == empty_board.read()

    def test_place_valid_queen(self):
        board = Chessboard()
        board.place_valid_queen()
        assert board.queens_are_valid()
