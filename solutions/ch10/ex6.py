# অধ্যায় ১০, অনুশীলনী ৬

import turtle

sizes = [10, 50, 100, 50, 10]
for size in sizes:
    for _ in range(4):
        turtle.forward(size)
        turtle.left(90)
    turtle.penup()
    turtle.forward(size + 10)
    turtle.pendown()

turtle.exitonclick()
