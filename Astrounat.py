import turtle as t

# Set up the turtle screen
t.speed(1)
t.bgcolor("black")
t.title("Astronaut")

# Draw the astronaut's helmet
t.penup()
t.goto(0, -100)
t.pendown()
t.color("white")
t.begin_fill()
t.circle(100)
t.end_fill()

# Draw the astronaut's body
t.penup()
t.goto(0, -100)
t.pendown()
t.color("white")
t.begin_fill()
t.left(90)
t.forward(200)
t.left(90)
t.forward(100)
t.left(90)
t.forward(200)
t.left(90)
t.forward(100)
t.end_fill()

# Draw the astronaut's faceplate
t.penup()
t.goto(30, 20)
t.pendown()
t.color("black")
t.begin_fill()
t.circle(45)
t.end_fill()

# Draw the astronaut's visor
t.penup()
t.goto(35, 25)
t.pendown()
t.color("white")
t.begin_fill()
t.circle(40)
t.end_fill()

# Draw the astronaut's antennas
t.penup()
t.goto(20, 90)
t.pendown()
t.color("white")
t.pensize(2)
t.goto(20, 150)
t.penup()
t.goto(50, 90)
t.pendown()
t.goto(50, 150)

# Close the drawing window on click
t.exitonclick()
