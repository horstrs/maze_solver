from graphics import Line, Point


class Cell:
    def __init__(self, window):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__x1 = -1
        self.__x2 = -1
        self.__y1 = -1
        self.__y2 = -1
        self.__win = window

    def draw(self, point_1, point_2):
        self.__x1 = point_1.x
        self.__y1 = point_1.y
        self.__x2 = point_2.x
        self.__y2 = point_2.y
        bottom_left = Point(self.__x1, self.__y1)
        bottom_right = Point(self.__x2, self.__y1)
        top_left = Point(self.__x1, self.__y2)
        top_right = Point(self.__x2, self.__y2)
        if self.has_left_wall:
            left_wall = Line(bottom_left, top_left)
            self.__win.draw_line(left_wall, "black")
        if self.has_top_wall:
            left_wall = Line(top_left, top_right)
            self.__win.draw_line(left_wall, "black")
        if self.has_right_wall:
            right_wall = Line(bottom_right, top_right)
            self.__win.draw_line(right_wall, "black")
        if self.has_bottom_wall:
            bottom_wall = Line(bottom_left, bottom_right)
            self.__win.draw_line(bottom_wall, "black")
