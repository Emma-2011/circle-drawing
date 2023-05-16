import turtle
t=turtle.Pen()
t.pensize(10)
t.pencolor("red")
t.circle(100)

t.penup()
t.goto(0,20)
t.pendown()
t.pencolor("orange")
t.circle(80)

t.penup()
t.goto(0,40)
t.pendown()
t.pencolor("yellow")
t.circle(60)

t.penup()
t.goto(0,60)
t.pendown()
t.pencolor("green")
t.circle(40)

t.penup()
t.goto(0,80)
t.pendown()
t.pencolor("blue")
t.circle(20)

t.penup()
t.goto(0,100)
t.pendown()
t.pencolor("purple")
t.circle(0)

t.hideturtle()
turtle.done()
