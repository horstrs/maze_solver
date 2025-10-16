import time

from cell import Cell
from graphics import Point

class Maze():
    def __init__(
            self,
            top_left_point,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win
            ):
        self.top_left = top_left_point
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self.cells = []
        self.__create_cells()
    
    def __create_cells(self):
        for i in range(self.num_cols):
            new_line = []
            for j in range(self.num_rows):
                new_cell = Cell(self.win)
                self.__draw_cell(new_cell, i, j)
                new_line.append(new_cell)
            self.cells.append(new_line)
            
    
    def __draw_cell(self, new_cell, i, j):
        top_left = self.__calculate_cell_top_left(i, j)
        bottom_right = self.__calculate_cell_bottom_right(i, j)
        new_cell.draw(top_left, bottom_right)
        self.__animate()

    def __calculate_cell_top_left(self, i, j):
        x = (self.cell_size_x * j + self.top_left.x)
        y = (self.cell_size_y * i + self.top_left.y)
        return Point(x, y)

    def __calculate_cell_bottom_right(self, i, j):
        x = (self.cell_size_x * (j+1) + self.top_left.x)
        y = (self.cell_size_y * (i+1) + self.top_left.y)
        return Point(x, y)

    def __animate(self):
        self.win.redraw()
        time.sleep(0.1)