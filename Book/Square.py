import turtle
turtle.shape("turtle")
turtle.speed(3)

for side_length in range (50, 100, 20):
    for i in range(3 ):
        turtle.forward(side_length)
        turtle.left(90)

turtle.exitonclick()