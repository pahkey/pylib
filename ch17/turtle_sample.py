import turtle as t


def draw_polygon(length, n):
    t.home()
    t.shape('turtle')
    t.color('red', 'yellow')
    t.begin_fill()
    for i in range(n):
        t.forward(length)
        t.left(360/n)
    t.end_fill()
    t.done()


draw_polygon(100, 5)
