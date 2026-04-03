import turtle
from turtle import *
speed(50)
bgcolor("black")
colours = ['orange', 'white']
for i in range(500):
    import colorsys
    goto(0, 0)
    color(colours[i % 2])
    forward(130)
    left(3)
    circle(40)
    forward(130)
    right(180)
done()

t = turtle.Turtle()
s = turtle.Screen().bgcolor('black')
t.speed(10)
n = 70
h = 0
for i in range(360):
    c = colorsys.hsv_to_rgb(h, 1, 0.8)
    h+= 1/n
    t.color(c)
    t.left(1)
    t.fd(1)
    for j in range(2):
        t.left(2)
        t.circle(10)

