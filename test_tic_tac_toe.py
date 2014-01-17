import unittest
from tic_tac_toe import TicTacToe

class TestTicTacToe(unittest.TestCase):
    def setUp(self):
        self.game = TicTacToe()

    def test_choose(self):
        self.game.choose(1, 1)
        expected = [' ', ' ', ' ', ' ', 'X', ' ', ' ', ' ', ' ']
        actual = self.game.get_board().get_data()
        self.assertEqual(actual, expected)

    def test_finished(self):
        self.game.choose(0, 0)
        self.game.choose(1, 0)
        self.game.choose(1, 1)
        self.game.choose(2, 2)
        self.game.choose(0, 1)
        self.game.choose(2, 1)
        self.game.choose(0, 2)
        actual = self.game.finished()
        expected = True
        self.assertEqual(actual, expected)
