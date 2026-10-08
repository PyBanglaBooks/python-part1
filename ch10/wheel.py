import turtle

turtle.speed(0)
counter = 0
while counter < 36:
    for _ in range(4):
        turtle.forward(100)
        turtle.right(90)
    turtle.right(10)
    counter += 1

turtle.exitonclick()
