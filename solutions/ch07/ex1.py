# অধ্যায় ৭, অনুশীলনী ১

import turtle

def draw_triangle(side):
    for _ in range(3):
        turtle.forward(side)
        turtle.left(120)

draw_triangle(100)
draw_triangle(150)
turtle.exitonclick()
