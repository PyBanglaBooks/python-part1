# অধ্যায় ১০, অনুশীলনী ৩

import turtle

for size in range(200, 0, -20):
    for _ in range(3):
        turtle.forward(size)
        turtle.left(120)

turtle.exitonclick()
