# TODO: Increase ball speed when paddle hits the ball
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

ORIGIN = 0
BORDER = 380
SKIP = 20
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
game_line = Turtle()
game_line.penup()
game_line.goto(x=ORIGIN, y=-BORDER)
game_line.color("gray")
game_line.setheading(90)
game_line.pendown()
scoreboard = Scoreboard()

for _ in range(0, BORDER):
    if game_line.ycor() >= 280:
        pass
    else:
        game_line.forward(SKIP)
        game_line.penup()
        game_line.forward(SKIP)
        game_line.pendown()

game_line.hideturtle()

# get paddle on:
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()

screen.listen()
# put paddle
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
game_is_on = True

while game_is_on:
    # time.sleep(.1)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with  paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # detect when Right paddle misses the ball
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # detect when left paddle misses the ball
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
