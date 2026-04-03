import turtle
import random

screen = turtle.Screen()
screen.bgcolor("skyblue")
screen.tracer(0)

# turtles
b = turtle.Turtle()   # balloons
b.hideturtle()
b.speed(0)

p = turtle.Turtle()   # peppa
p.hideturtle()
p.speed(0)

# --------------------
# BALLOONS
# --------------------
colors = ["red", "yellow", "green", "blue", "pink", "orange"]

balloons = []
for i in range(8):
    balloons.append([
        random.randint(-250, 250),
        random.randint(-200, 0),
        random.choice(colors),
        random.uniform(0.5, 2)
    ])

def draw_balloons():
    b.clear()
    for x, y, color, speed in balloons:
        b.penup()
        b.goto(x, y)
        b.pendown()
        b.color(color)
        b.begin_fill()
        b.circle(20)
        b.end_fill()

        b.setheading(-90)
        b.forward(40)

def move_balloons():
    for balloon in balloons:
        balloon[1] += balloon[3]
        if balloon[1] > 250:
            balloon[1] = -200

# --------------------
# DRAW CHARACTER
# --------------------
def draw_character(x, y, body_color, blink=False):
    p.penup()
    p.goto(x, y)
    p.pendown()

    # head
    p.color("pink")
    p.begin_fill()
    p.circle(35)
    p.end_fill()

    # snout
    p.penup()
    p.goto(x+35, y+10)
    p.pendown()
    p.begin_fill()
    p.circle(12)
    p.end_fill()

    # eyes
    for ex, ey in [(x-10, y+45), (x+10, y+45)]:
        p.penup()
        p.goto(ex, ey)
        p.pendown()

        if blink:
            # closed eye (line)
            p.setheading(0)
            p.forward(10)
        else:
            # open eye
            p.color("white")
            p.begin_fill()
            p.circle(6)
            p.end_fill()

            p.color("black")
            p.penup()
            p.goto(ex+2, ey+2)
            p.pendown()
            p.begin_fill()
            p.circle(2)
            p.end_fill()

    # smile
    p.penup()
    p.goto(x-10, y+20)
    p.setheading(-60)
    p.pendown()
    p.circle(15, 120)

    # body
    p.penup()
    p.goto(x-20, y-40)
    p.pendown()
    p.color(body_color)
    p.begin_fill()
    for _ in range(2):
        p.forward(40)
        p.right(90)
        p.forward(40)
        p.right(90)
    p.end_fill()

# --------------------
# TEXT
# --------------------
def draw_text():
    p.penup()
    p.goto(0, 180)
    p.color("purple")
    p.write("Surprise! 🎉", align="center", font=("Arial", 24, "bold"))

# --------------------
# ANIMATION LOOP
# --------------------
frame = 0

while True:
    p.clear()

    # blinking logic
    blink = (frame % 40 < 5)

    # draw characters
    draw_character(-80, -20, "red", blink)   # Peppa
    draw_character(80, -20, "blue", blink)   # George

    draw_text()

    move_balloons()
    draw_balloons()

    screen.update()
    frame += 1
