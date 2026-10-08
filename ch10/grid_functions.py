import turtle

def draw_square(size):
    for _ in range(4):
        turtle.forward(size)
        turtle.left(90)

def draw_row():
    for _ in range(3):
        draw_square(50)
        turtle.penup()
        turtle.forward(60)
        turtle.pendown()

def next_row():
    turtle.penup()
    turtle.backward(180)
    turtle.right(90)
    turtle.forward(60)
    turtle.left(90)
    turtle.pendown()

turtle.speed(0)
for _ in range(3):
    draw_row()
    next_row()

turtle.exitonclick()
