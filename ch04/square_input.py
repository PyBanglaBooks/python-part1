import turtle

size = int(input("How big should the square be? "))
color_name = input("What color? (red, blue, green): ")

turtle.color(color_name)
turtle.forward(size)
turtle.left(90)
turtle.forward(size)
turtle.left(90)
turtle.forward(size)
turtle.left(90)
turtle.forward(size)
turtle.left(90)
turtle.exitonclick()
