import turtle
import random

# Screen
wn = turtle.Screen()
wn.title("😂 Catch the Crazy Emoji")
wn.setup(width=800, height=600)

# Create gradient-like background with multiple colored rectangles
bg = turtle.Turtle()
bg.hideturtle()
bg.speed(0)
bg.penup()

# Draw gradient background from top to bottom
gradient_colors = ["#FF6B9D", "#FFA07A", "#FFD700", "#98D8C8", "#6BB6FF"]
y_pos = 300
rect_height = 120

for color in gradient_colors:
    bg.goto(-400, y_pos)
    bg.pendown()
    bg.fillcolor(color)
    bg.begin_fill()
    for _ in range(2):
        bg.forward(800)
        bg.right(90)
        bg.forward(rect_height)
        bg.right(90)
    bg.end_fill()
    bg.penup()
    y_pos -= rect_height

# Add some stars/sparkles
bg.color("white")
for _ in range(30):
    x = random.randint(-380, 380)
    y = random.randint(-280, 280)
    bg.goto(x, y)
    bg.dot(random.randint(3, 8))

# Score
score = 0

# Pen for score
pen = turtle.Turtle()
pen.hideturtle()
pen.penup()
pen.goto(0, 260)
pen.color("white")
pen.write("Score: 0", align="center", font=("Comic Sans MS", 24, "bold"))

# Create compound emoji (face with features as one unit)
class EmojiCharacter:
    def __init__(self):
        self.parts = []
        self.create_emoji()
    
    def create_emoji(self):
        # Main face
        face = turtle.Turtle()
        face.hideturtle()
        face.speed(0)
        face.penup()
        
        # Left eye
        left_eye = turtle.Turtle()
        left_eye.hideturtle()
        left_eye.speed(0)
        left_eye.penup()
        
        # Right eye
        right_eye = turtle.Turtle()
        right_eye.hideturtle()
        right_eye.speed(0)
        right_eye.penup()
        
        # Mouth
        mouth = turtle.Turtle()
        mouth.hideturtle()
        mouth.speed(0)
        mouth.penup()
        
        self.parts = [face, left_eye, right_eye, mouth]
    
    def draw_at(self, x, y):
        face, left_eye, right_eye, mouth = self.parts
        
        # Clear all parts
        for part in self.parts:
            part.clear()
        
        # Draw face (yellow circle with border)
        face.goto(x, y - 35)
        face.pendown()
        face.pensize(3)
        face.pencolor("#FF8C00")
        face.fillcolor("#FFD700")
        face.begin_fill()
        face.circle(35)
        face.end_fill()
        face.penup()
        
        # Draw left eye
        left_eye.goto(x - 15, y + 8)
        left_eye.pendown()
        left_eye.fillcolor("black")
        left_eye.begin_fill()
        left_eye.circle(5)
        left_eye.end_fill()
        left_eye.penup()
        
        # Draw right eye
        right_eye.goto(x + 15, y + 8)
        right_eye.pendown()
        right_eye.fillcolor("black")
        right_eye.begin_fill()
        right_eye.circle(5)
        right_eye.end_fill()
        right_eye.penup()
        
        # Draw smile
        mouth.goto(x - 18, y - 5)
        mouth.pendown()
        mouth.pensize(4)
        mouth.pencolor("#FF1493")
        mouth.setheading(-60)
        mouth.circle(18, 120)
        mouth.penup()

# Create emoji character
emoji_char = EmojiCharacter()

# Invisible clickable turtle
emoji = turtle.Turtle()
emoji.shape("circle")
emoji.color("#FFD700")
emoji.shapesize(3.5, 3.5)
emoji.penup()
emoji.goto(0, 0)

# Draw initial emoji
emoji_char.draw_at(0, 0)

# Funny messages
messages = [
    "😂 Got me!",
    "😜 Too slow!",
    "🤣 Ouch!",
    "😆 Catch me again!",
    "😝 That tickles!"
]

# Message writer
msg_pen = turtle.Turtle()
msg_pen.hideturtle()
msg_pen.penup()
msg_pen.goto(0, -250)
msg_pen.color("white")

# Move emoji randomly
def move_emoji():
    x = random.randint(-280, 280)
    y = random.randint(-180, 180)
    emoji.goto(x, y)
    emoji_char.draw_at(x, y)

# When clicked
def clicked(x, y):
    global score
    score += 1

    # Update score
    pen.clear()
    pen.write(f"Score: {score}", align="center", font=("Comic Sans MS", 24, "bold"))

    # Funny message
    msg_pen.clear()
    msg_pen.write(random.choice(messages), align="center", font=("Comic Sans MS", 18, "bold"))

    # Move emoji
    move_emoji()

# Click event
emoji.onclick(clicked)

# Keep moving automatically
def auto_move():
    move_emoji()
    wn.ontimer(auto_move, 800)  # moves every 0.8 sec

auto_move()

wn.mainloop()

# Made with Bob
