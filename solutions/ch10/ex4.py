# অধ্যায় ১০, অনুশীলনী ৪

import turtle

turtle.speed(0)
turtle.penup()
for row in range(5):
    for col in range(5):
        turtle.dot(10)
        turtle.forward(40)
    # back to the left, one step down
    turtle.backward(200)
    turtle.right(90)
    turtle.forward(40)
    turtle.left(90)

turtle.exitonclick()
