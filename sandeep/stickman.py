import turtle

t = turtle.Turtle()
screen = turtle.Screen()

# Setup
screen.bgcolor("lightblue")
t.pensize(3)
t.speed(5)

# --------------------
# HEAD
# --------------------
t.penup()
t.goto(0, 100)
t.pendown()
t.circle(50)

# --------------------
# EYES
# --------------------
# Left eye
t.penup()
t.goto(-20, 150)
t.pendown()
t.dot(10)

# Right eye
t.penup()
t.goto(20, 150)
t.pendown()
t.dot(10)

# --------------------
# MOUTH
# --------------------
t.penup()
t.goto(-20, 120)
t.setheading(-60)
t.pendown()
t.circle(25, 120)

# --------------------
# BODY
# --------------------
t.penup()
t.goto(0, 100)
t.setheading(-90)
t.pendown()
t.forward(100)

# --------------------
# ARMS
# --------------------
t.penup()
t.goto(0, 50)
t.pendown()

# Left arm
t.setheading(160)
t.forward(60)

# Back to center
t.penup()
t.goto(0, 50)
t.pendown()

# Right arm
t.setheading(20)
t.forward(60)

# --------------------
# LEGS
# --------------------
t.penup()
t.goto(0, 0)
t.pendown()

# Left leg
t.setheading(-120)
t.forward(70)

# Back to center
t.penup()
t.goto(0, 0)
t.pendown()

# Right leg
t.setheading(-60)
t.forward(70)

# --------------------
# FINISH
# --------------------
turtle.done()
