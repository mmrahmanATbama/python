
"""
my thoughts
Pong game:
1. setup:
    a. divide the screen
    b. have two score
    c. two bats that can slide only one around the line
    d. ball bounces on the side wall but goes past behind the bat.

2. when the ball touches side of the wall, it bounces
3. when the ball touches bat, it bounces
4. when the ball goes behind the bat the other player gets a score, a new ball is set.


Classes:
1. keep score for both players
2. ball movement
3. players movement

Question when does the game end?
can you pause the game?


Angela Note:
1. Create the screen
2. Create and move paddle
3. Create another paddle
4. Create the ball and make it move
5. Detect collision with wall and bounce
6. Detect collision with paddle
7. Detect when paddle misses
8. Keep score

"""

from turtle import Screen, Turtle
ORIGIN = 0
BORDER = 280
SKIP = 20
screen = Screen()
screen.setup(width=600,height=600)
screen.title("Pong")
screen.tracer(0)
game_line = Turtle()
game_line.penup()
game_line.goto(x=ORIGIN, y=-BORDER)
game_line.color("gray")
game_line.setheading(90)
game_line.pendown()
game_line.goto(x=ORIGIN, y=BORDER)


screen.exitonclick()