# অধ্যায় ১৪, অনুশীলনী ১

import turtle
import random

sizes = [5, 10, 20]

turtle.penup()
turtle.speed(0)
for _ in range(50):
    x = random.randint(-150, 150)
    y = random.randint(-150, 150)
    turtle.setposition(x, y)
    size = random.choice(sizes)
    turtle.dot(size)

turtle.exitonclick()
