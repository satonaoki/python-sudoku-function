import unittest
import sudoku

class TestSudoku(unittest.TestCase):
    def test_solve(self):
        input = ".........16.....578..6.3..43..5.4..1.2..9..6...8...5....7...2.....7.6......341..."

        output = [[7, 9, 3, 4, 1, 5, 6, 8, 2], [1, 6, 4, 2, 8, 9, 3, 5, 7], [8, 5, 2, 6, 7, 3, 9, 1, 4], [3, 7, 9, 5, 6, 4, 8, 2, 1], [5, 2, 1, 8, 9, 7, 4, 6, 3], [6, 4, 8, 1, 3, 2, 5, 7, 9], [4, 1, 7, 9, 5, 8, 2, 3, 6], [9, 3, 5, 7, 2, 6, 1, 4, 8], [2, 8, 6, 3, 4, 1, 7, 9, 5]]

        self.assertEqual(sudoku.sudoku(input), output)

if __name__ == '__main__':
    unittest.main()
