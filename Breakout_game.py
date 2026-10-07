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
pad.shapesize(stretch_wid=1, stretch_len=5)
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

def update_score():
    score_display.clear()   
    score_display.write(f"SCORE.{score}, LIVES:{5-death}",align="center",font=("Arial",24,"bold"))

update_score()
game_started=False

def start_game(x,y):
    global game_started
    game_started=True

sc.onclick(start_game)

#moment
def move_left():
    x=pad.xcor()
    if x > -250:
        pad.setx(x-60)

def move_right():
    x=pad.xcor()
    if x < 250:
        pad.setx(x+60)

sc.listen()
sc.onkey(move_left, "a")
sc.onkey(move_right, "d")

move_left()
move_right()

#maingame loop
while True:
    sc.update()
    time.sleep(0.01)
    if not game_started:
        continue
    
    #move ball
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    #wall collision
    if ball.xcor()> 290 or ball.xcor() < -290:
        ball.dx*=-1
    if ball.ycor()> 290:
        ball.dy*=-1

    #bottom collision
    if ball.ycor() < -290:
        death+=1
        ball.goto(0,0)
        ball.dy*=-1
        game_started=False
        update_score()

        if death ==5:
            score_display.goto(0,0)
            score_display.write("GAME OVER", align="center"
                                ,font=("Arial",30,"bold"))


            break
    #paddle collision
    if (-260 < ball.ycor() < -230) and\
        (pad.xcor() -50<ball.xcor() <pad.xcor() +50):
        ball.dy*=-1
        




sc.mainloop()
