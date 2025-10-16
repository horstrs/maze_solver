from graphics import Window, Point, Line

def main():
    win = Window(800, 600)
    point_1 = Point(5, 5)
    point_2 = Point(5, 100)
    point_3 = Point(100, 5)
    line_1 = Line(point_1, point_2)
    line_1.draw(win.canvas_widget, "black")
    line_2 = Line(point_1, point_3)
    line_2.draw(win.canvas_widget, "red")
    line_3 = Line(point_2, point_3)
    line_3.draw(win.canvas_widget, "gray")

    win.wait_for_close()


if __name__ == "__main__":
    main()
