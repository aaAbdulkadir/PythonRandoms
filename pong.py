#! Abdulkadir - Pong

import turtle

# score
score_1 = 0
score_2 = 0

# initialising screen
screen = turtle.Screen()
screen.title("Pong by Abdulkadir")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

# paddle 1
paddle_1 = turtle.Turtle()
paddle_1.speed(0) # animation speed
paddle_1.shape("square")
paddle_1.shapesize(stretch_wid=5, stretch_len=1)
paddle_1.color("white")
paddle_1.penup()    # doesnt draw a line as it moves
paddle_1.goto(-350, 0)

# paddle 2
paddle_2 = turtle.Turtle()
paddle_2.speed(0)
paddle_2.shape("square")
paddle_2.shapesize(stretch_wid=5, stretch_len=1)
paddle_2.color("white")
paddle_2.penup()
paddle_2.goto(350, 0)

# ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)

# pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write(f"Player 1: {score_1} | Player 2: {score_2}", align="center", font=("Courier", 24, "normal"))

# change in ball
ball.dx = 2
ball.dy = 2

# paddles movement using keys
def paddle_1_up():
    y = paddle_1.ycor() # returns y position
    y += 20
    paddle_1.sety(y)

def paddle_1_down():
    y = paddle_1.ycor() # returns y position
    y -= 20
    paddle_1.sety(y)

def paddle_2_up():
    y = paddle_2.ycor() # returns y position
    y += 20
    paddle_2.sety(y)

def paddle_2_down():
    y = paddle_2.ycor() # returns y position
    y -= 20
    paddle_2.sety(y)

# keyboard binding
screen.listen() # listen for keyboard inputs
screen.onkey(paddle_1_up, "w")
screen.onkey(paddle_1_down, "s")
screen.onkey(paddle_2_up, "Up")
screen.onkey(paddle_2_down, "Down")

# game
while True:
    screen.update()

    # move ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # close the borders
    # top border
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    # bottom border
    if ball.ycor() < -280:
        ball.sety(-280)
        ball.dy *= -1
    # right border
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_1 += 1
        pen.clear()
        pen.write(f"Player 1: {score_1} | Player 2: {score_2}", align="center", font=("Courier", 24, "normal"))
    # right border
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_2 += 1
        pen.clear()
        pen.write(f"Player 1: {score_1} | Player 2: {score_2}", align="center", font=("Courier", 24, "normal"))

    # paddle and ball collision
    # right paddle
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_2.ycor() + 40 and ball.ycor() > paddle_2.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
    # left paddle
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_1.ycor() + 40 and ball.ycor() > paddle_1.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
