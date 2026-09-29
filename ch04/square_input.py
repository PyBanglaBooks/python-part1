import turtle

size = int(input("How big should the square be? "))
pen = int(input("How thick should the pen be? (1-10): "))

turtle.width(pen)
turtle.forward(size)
turtle.left(90)
turtle.forward(size)
turtle.left(90)
turtle.forward(size)
turtle.left(90)
turtle.forward(size)
turtle.left(90)
turtle.exitonclick()
