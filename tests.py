import unittest

from maze import Maze
from graphics import Point

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        top_left = Point(0, 0)
        m1 = Maze(top_left, num_rows, num_cols, 10, 10)
        self.assertEqual(len(m1._Maze__cells), num_rows)
        self.assertEqual(len(m1._Maze__cells[0]), num_cols)
        self.assertFalse(m1._Maze__cells[0][0].has_top_wall)
        self.assertFalse(m1._Maze__cells[num_rows-1][num_cols-1].has_bottom_wall)

if __name__ == "__main__":
    unittest.main()