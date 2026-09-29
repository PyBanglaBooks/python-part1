import turtle
import random

turtle.penup()
turtle.speed(0)
for i in range(50):
    x = random.randint(-150, 150)
    y = random.randint(-150, 150)
    turtle.setposition(x, y)
    size = random.randint(5, 25)
    turtle.dot(size)

turtle.exitonclick()
