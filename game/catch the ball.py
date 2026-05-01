import turtle
import random

# Screen setup
wn = turtle.Screen()
wn.title("Catch the Ball Game")
wn.bgcolor("lightblue")
wn.setup(width=600, height=600)
wn.tracer(0)

# Paddle
paddle = turtle.Turtle()
paddle.shape("square")
paddle.color("black")
paddle.shapesize(stretch_wid=1, stretch_len=5)
paddle.penup()
paddle.goto(0, -250)

# Ball
ball = turtle.Turtle()
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(0, 250)

ball.dy = -0.7

# Paddle movement tracking
paddle_dx = 0
paddle_speed = 1.5

# Score
score = 0
pen = turtle.Turtle()
pen.hideturtle()
pen.penup()
pen.goto(0, 260)
pen.write("Score: 0", align="center", font=("Arial", 16, "bold"))

# Move paddle functions
def start_move_left():
    global paddle_dx
    paddle_dx = -paddle_speed

def start_move_right():
    global paddle_dx
    paddle_dx = paddle_speed

def stop_move():
    global paddle_dx
    paddle_dx = 0

# Keyboard controls
wn.listen()
wn.onkeypress(start_move_left, "Left")
wn.onkeypress(start_move_right, "Right")
wn.onkeyrelease(stop_move, "Left")
wn.onkeyrelease(stop_move, "Right")

# Game loop
while True:
    wn.update()

    # Move paddle continuously
    x = paddle.xcor()
    x += paddle_dx
    if x < -250:
        x = -250
    if x > 250:
        x = 250
    paddle.setx(x)

    # Move ball
    ball.sety(ball.ycor() + ball.dy)

    # Ball reaches bottom (miss)
    if ball.ycor() < -300:
        ball.goto(random.randint(-250, 250), 250)

    # Catch ball
    if (ball.ycor() < -230 and ball.ycor() > -260) and \
       (paddle.xcor() - 50 < ball.xcor() < paddle.xcor() + 50):

        ball.goto(random.randint(-250, 250), 250)
        score += 1
        pen.clear()
        pen.write(f"Score: {score}", align="center", font=("Arial", 16, "bold"))
