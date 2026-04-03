import turtle

t = turtle.Turtle()
screen = turtle.Screen()

# Setup
screen.bgcolor("white")
t.color("black")
t.speed(0)
t.pensize(2)

# --------------------
# HEAD
# --------------------
t.penup()
t.goto(0, 50)
t.pendown()
t.circle(60)

# --------------------
# EYES
# --------------------
for x in [-20, 20]:
    t.penup()
    t.goto(x, 120)
    t.pendown()
    t.circle(5)

# --------------------
# NOSE
# --------------------
t.penup()
t.goto(0, 110)
t.setheading(-90)
t.pendown()
t.forward(10)

# --------------------
# MOUTH
# --------------------
t.penup()
t.goto(-20, 90)
t.setheading(-60)
t.pendown()
t.circle(25, 120)

# --------------------
# HAIR (controlled strokes)
# --------------------
t.penup()
t.goto(-50, 160)
t.setheading(-60)
t.pendown()

for i in range(20):
    t.forward(40)
    t.backward(40)
    t.left(6)

# --------------------
# NECK
# --------------------
for x in [-15, 15]:
    t.penup()
    t.goto(x, 50)
    t.setheading(-90)
    t.pendown()
    t.forward(30)

# --------------------
# SHOULDERS
# --------------------
t.penup()
t.goto(-60, 20)
t.setheading(0)
t.pendown()
t.forward(120)

# --------------------
# LIGHT SHADING (horizontal only)
# --------------------
t.penup()
t.goto(-40, 80)

for i in range(10):
    t.goto(-40, 80 - i*3)
    t.pendown()
    t.forward(80)
    t.penup()

# --------------------
# FINISH
# --------------------
turtle.done()
