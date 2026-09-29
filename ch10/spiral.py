import turtle

turtle.speed(0)
widths = [1, 3, 6]

for i in range(40):
    turtle.width(widths[i % len(widths)])
    turtle.forward(i * 5)
    turtle.left(91)

turtle.exitonclick()
