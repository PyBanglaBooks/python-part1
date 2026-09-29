import turtle

for col in range(3):
    for side in range(4):
        turtle.forward(50)
        turtle.left(90)
    turtle.penup()
    turtle.forward(60)
    turtle.pendown()

turtle.exitonclick()
