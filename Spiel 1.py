import turtle
import time

wn = turtle.Screen()
wn.title("Pong by @jeronimofinke")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 2  # Reduce speed of the ball
ball.dy = 2  # Reduce speed of the ball

# Functions
def paddle_a_up():
    y = paddle_a.ycor()
    if y < 250:  # Limit to the upper boundary
        y += 20
        paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    if y > -240:  # Limit to the lower boundary
        y -= 20
        paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    if y < 250:  # Limit to the upper boundary
        y += 20
        paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    if y > -240:  # Limit to the lower boundary
        y -= 20
        paddle_b.sety(y)    

# Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Spieler A: 0  Spieler B: 0", align="center", font=("Courier", 24, "normal")) 

# Main game loop
while True:
    wn.update()
    
    # Add a delay to slow down the game
    time.sleep(0.01)  # Adjust the value to control the speed of the game loop

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1        
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Spieler A: {}  Spieler B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal")) 
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1  
        score_b += 1
        pen.clear()
        pen.write("Spieler A: {}  Spieler B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal")) 

    # Paddle and ball collisions
    if ball.xcor() > 340 and ball.xcor() < 350 and ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 50:
        ball.setx(340)
        ball.dx *= -1
    if ball.xcor() < -340 and ball.xcor() > -350 and ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 50:
        ball.setx(-340)
        ball.dx *= -1
