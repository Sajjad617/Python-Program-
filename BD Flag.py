
import turtle
screen=turtle.getscreen()
t=turtle
t.begin_fill()
t.color('green')
t.forward(-200)
t.forward(400)
t.left(90)
t.forward(200)
t.left(90)
t.forward(400)
t.left(90)
t.forward(200)
t.end_fill()
tt=turtle
tt.begin_fill()
tt.color('green')
tt.goto(-50,100)
tt.circle(50)
tt.color('red')
tt.end_fill()
t.exitonclick()