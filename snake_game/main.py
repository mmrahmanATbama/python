import time
from turtle import Screen, Turtle
from snake import Snake
from score import Score
from food import Food

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

border_line = 270
border = Turtle()
border.color("green")
border.penup()
border.goto(border_line, -border_line)
border.setheading(90)
border.pendown()
border.goto(border_line, border_line)
border.goto(-border_line, border_line)
border.goto(-border_line, -border_line)
border.goto(border_line, -border_line)
border.penup()
border.hideturtle()

spacer = Turtle()
spacer.color("red")
spacer.penup()
spacer.goto(0, 0)
spacer.pendown()
spacer.write("Press Space to start", False, align="Center", font=('Courier', 20, 'normal'))
spacer.hideturtle()
snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


# animate the snake, so it moves across the screen
def click_handler():
    spacer.clear()
    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(0.1)
        snake.move()

        # collision with food
        if snake.head.distance(food) < 15:
            food.refresh()
            snake.extend()
            score.refresh()

        # collision with wall
        if snake.head.xcor() > 270 or snake.head.xcor() < -270 or snake.head.ycor() > 270 or snake.head.ycor() < -270:
            score.reset_score()
            snake.reset_snake()
        # Detect collision with tail
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                score.reset_score()
                snake.reset_snake()


# screen.exitonclick()
screen.onkey(click_handler, "space")
screen.mainloop()
