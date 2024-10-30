import turtle
turtle.color('red')
for i in range(10):
    turtle.forward(10)
    turtle.penup()
    turtle.forward(10)
    turtle.pendown()

turtle.circle(100)

turtle.exitonclick()
