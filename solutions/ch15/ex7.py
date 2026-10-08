# অধ্যায় ১৫, অনুশীলনী ৭

import turtle

fibs = [1, 1, 2, 3, 5, 8, 13]

turtle.speed(0)
for f in fibs:
    side = f * 10
    for _ in range(4):
        turtle.forward(side)
        turtle.left(90)
    turtle.circle(side, 90)

turtle.exitonclick()
