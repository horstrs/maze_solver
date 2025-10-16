from graphics import Window, Point, Line, Cell

def main():
    win = Window(800, 600)
    point_1 = Point(5, 5)
    point_2 = Point(40, 40)

    point_3 = Point(40, 5)
    point_4 = Point(75, 40)
    
    cell1 = Cell(win)
    cell1.draw(point_1, point_2)
    cell2 = Cell(win)
    cell2.draw(point_3, point_4)


    c = Cell(win)
    c.has_left_wall = False
    c.draw(Point(50, 50), Point(100, 100))

    c = Cell(win)
    c.has_right_wall = False
    c.draw(Point(125, 125), Point(200, 200))

    c = Cell(win)
    c.has_bottom_wall = False
    c.draw(Point(225, 225), Point(250, 250))

    c = Cell(win)
    c.has_top_wall = False
    c.draw(Point(300, 300), Point(500, 500))

    win.wait_for_close()


if __name__ == "__main__":
    main()
