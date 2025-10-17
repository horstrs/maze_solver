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
            win=None
            ):
        self.__top_left = top_left_point
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = win
        self.__cells = []
        self.__create_cells()
    
    def __create_cells(self):
        for i in range(self.__num_cols):
            new_line = []
            for j in range(self.__num_rows):
                new_cell = Cell(self.__win)
                self.__draw_cell(new_cell, i, j)
                new_line.append(new_cell)
            self.__cells.append(new_line)
            
    
    def __draw_cell(self, new_cell, i, j):
        top_left = self.__calculate_cell_top_left(i, j)
        bottom_right = self.__calculate_cell_bottom_right(i, j)
        new_cell.draw(top_left, bottom_right)
        self.__animate()

    def __calculate_cell_top_left(self, i, j):
        x = (self.__cell_size_x * j + self.__top_left.x)
        y = (self.__cell_size_y * i + self.__top_left.y)
        return Point(x, y)

    def __calculate_cell_bottom_right(self, i, j):
        x = (self.__cell_size_x * (j+1) + self.__top_left.x)
        y = (self.__cell_size_y * (i+1) + self.__top_left.y)
        return Point(x, y)

    def __animate(self):
        if self.__win is not None:
            self.__win.redraw()
            time.sleep(0.1)