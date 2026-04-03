import turtle

t = turtle.Turtle()
screen = turtle.Screen()

# Setup
screen.bgcolor("#e6f2ff")  # light sky
t.speed(0)
t.pensize(2)
t.color("black", "white")  # outline + fill

# --------------------
# FUNCTION: RECTANGLE WITH FILL
# --------------------
def rectangle(w, h):
    t.begin_fill()
    for _ in range(2):
        t.forward(w)
        t.left(90)
        t.forward(h)
        t.left(90)
    t.end_fill()

# --------------------
# BASE PLATFORM
# --------------------
t.penup()
t.goto(-250, -120)
t.pendown()
rectangle(500, 120)

# --------------------
# MAIN BUILDING
# --------------------
t.penup()
t.goto(-180, 0)
t.pendown()
rectangle(360, 180)

# --------------------
# MAIN DOME (better curve)
# --------------------
t.penup()
t.goto(0, 180)
t.setheading(0)
t.pendown()

t.begin_fill()
t.circle(90)
t.end_fill()

# top spike
t.left(90)
t.forward(50)

# --------------------
# SIDE DOMES
# --------------------
def small_dome(x):
    t.penup()
    t.goto(x, 140)
    t.setheading(0)
    t.pendown()

    t.begin_fill()
    t.circle(50)
    t.end_fill()

small_dome(-120)
small_dome(120)

# --------------------
# MAIN ARCH (DOOR)
# --------------------
t.penup()
t.goto(-60, 0)
t.setheading(90)
t.pendown()

t.begin_fill()
t.circle(60, 180)
t.forward(120)
t.left(90)
t.forward(120)
t.left(90)
t.forward(120)
t.end_fill()

# --------------------
# WINDOWS (arches)
# --------------------
for x in [-120, -60, 60, 120]:
    t.penup()
    t.goto(x, 50)
    t.setheading(90)
    t.pendown()
    t.circle(25, 180)

# --------------------
# MINARETS (realistic style)
# --------------------
def minaret(x):
    t.penup()
    t.goto(x, -120)
    t.setheading(90)
    t.pendown()

    # tower body
    t.forward(260)

    # small dome cap
    t.begin_fill()
    t.circle(15)
    t.end_fill()

# 4 minarets
minaret(-230)
minaret(-180)
minaret(180)
minaret(230)

# --------------------
# DECOR LINES
# --------------------
for y in [70, 120]:
    t.penup()
    t.goto(-180, y)
    t.setheading(0)
    t.pendown()
    t.forward(360)

# --------------------
# FINISH
# --------------------
t.hideturtle()
turtle.done()
