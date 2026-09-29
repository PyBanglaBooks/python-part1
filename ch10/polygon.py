import turtle

widths = [1, 3, 5, 7, 9, 11]
sides = len(widths)
angle = 360 / sides

for w in widths:
    turtle.width(w)
    turtle.forward(80)
    turtle.left(angle)

turtle.exitonclick()
