import turtle
turtle.color("black")
turtle.speed(10)
counter = 0
while counter < 36:
    for i in range (4):
        turtle.forward(100)
        turtle.right(90)
    turtle.right(7)
    counter += 1

turtle.exitonclick()