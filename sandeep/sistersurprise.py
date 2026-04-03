import turtle
import colorsys

# Setup screen
screen = turtle.Screen()
screen.bgcolor("black")

t = turtle.Turtle()
t.speed(0)
t.width(3)

# --------------------
# RAINBOW SPIRAL
# --------------------
h = 0

for i in range(200):
    color = colorsys.hsv_to_rgb(h, 1, 1)
    t.pencolor(color)
    h += 0.01

    t.forward(i)
    t.left(59)

# --------------------
# WRITE MESSAGE
# --------------------
t.penup()
t.goto(0, 0)
t.color("white")

t.write("I ❤️ You!", align="center", font=("Arial", 24, "bold"))

# --------------------
# FINISH
# --------------------
t.hideturtle()
turtle.done()
