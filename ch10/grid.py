import turtle

turtle.speed(0)
for row in range(3):
    for col in range(3):
        for side in range(4):
            turtle.forward(50)
            turtle.left(90)
        turtle.penup()
        turtle.forward(60)
        turtle.pendown()
    # সারি শেষ: বাঁয়ে ফিরে এক ধাপ নিচে নামা
    turtle.penup()
    turtle.backward(180)
    turtle.right(90)
    turtle.forward(60)
    turtle.left(90)
    turtle.pendown()

turtle.exitonclick()
