# অধ্যায় ১০, অনুশীলনী ২

import turtle

def draw_polygon(widths, length):
    angle = 360 / len(widths)
    for w in widths:
        turtle.width(w)
        turtle.forward(length)
        turtle.left(angle)

def move_right(distance):
    turtle.penup()
    turtle.forward(distance)
    turtle.pendown()

draw_polygon([1, 4, 8], 80)
move_right(110)
draw_polygon([1, 3, 5, 7], 60)
move_right(90)
draw_polygon([1, 2, 3, 4, 5, 6, 7, 8], 30)
turtle.exitonclick()
