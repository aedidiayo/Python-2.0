import turtle
import time
sc=turtle.Screen()
sc.setup(600,800)
sc.bgcolor("black")
sc.title("Brick Breaker")
sc.tracer(0)
#screen automation or updation

#paddle
pad=turtle.Turtle()
pad.color("red")
pad.shape("square")
pad.shapesize()
pad.penup()
pad.goto(0,-250)
pad.width=100

#ball
ball=turtle.Turtle()
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(1,300)
ball.dx=3
ball.dy=-3

#bricks
bricks=[]
colors=["green", "purple", "blue", "orange"]
for row in range(4):
    for col in range(-240,241,80):
        brick=turtle.Turtle()
        brick.shape("square")
        brick.color(colors[row])
        brick.shapesize(stretch_wid=1,stretch_len=3)
        brick.penup()
        brick.goto(col,150 - (row*40))
        bricks.append(brick)

#score
score=0
death=0
score_display=turtle.Turtle()
score_display.hideturtle()
score_display.color("yellow")
score_display.penup()
score_display.goto(50,200)
