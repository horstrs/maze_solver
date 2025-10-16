from tkinter import Tk, BOTH, Canvas


class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.__root_widget = Tk()
        self.__root_widget.title("Maze Solver")
        self.__root_widget.protocol("WM_DELETE_WINDOW", self.close)
        self.canvas_widget = Canvas(self.__root_widget, height=height, width=width)
        self.canvas_widget.pack(fill=BOTH, expand=1)
        self.__running = False

    def redraw(self):
        self.__root_widget.update_idletasks()
        self.__root_widget.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
        print("window closed...")

    def close(self):
        self.__running = False

    def draw_line(self, line, fill_color):
        line.draw(self.canvas_widget, fill_color)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line:
    def __init__(self, point_1, point_2):
        self.point_1 = point_1
        self.point_2 = point_2

    def draw(self, canvas, fill_color):
        canvas.create_line(
            self.point_1.x,
            self.point_1.y,
            self.point_2.x,
            self.point_2.y,
            fill=fill_color,
            width=2,
        )


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
