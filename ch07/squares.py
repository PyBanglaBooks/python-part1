import turtle

def draw_square(side_length):
    for _ in range(4):
        turtle.forward(side_length)
        turtle.left(90)

turtle.speed(0)
for _ in range(90):
    draw_square(100)
    turtle.right(4)
turtle.exitonclick()
