import turtle

widths = [1, 4, 7, 10]

for w in widths:
    turtle.width(w)
    turtle.forward(100)
    turtle.left(90)

turtle.exitonclick()
