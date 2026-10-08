# অধ্যায় ৪, অনুশীলনী ৪

import turtle

pole = 200
size = 60

# the pole: face up and go to the top
turtle.left(90)
turtle.forward(pole)

# the flag: three sides, the pole makes the fourth
turtle.right(90)
turtle.forward(size)
turtle.right(90)
turtle.forward(size)
turtle.right(90)
turtle.forward(size)

turtle.exitonclick()
