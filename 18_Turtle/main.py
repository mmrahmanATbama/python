import random
from turtle import Turtle, Screen, color, colormode
from random import randint

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("red")
# Draw a squre
# for _ in range(4):
#     timmy_the_turtle.forward(100.0)
#     timmy_the_turtle.left(90)

# Draw a dashed line
# for _ in range(50):
#     timmy_the_turtle.forward(10.0)
#     timmy_the_turtle.penup()
#     timmy_the_turtle.forward(10.0)
#     timmy_the_turtle.down()


# Draw different shapes
# for _ in range(3):
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.right(60)
colormode(255)
# for i in range(3, 10):
#     angle = 360 // i
timmy_the_turtle.color(randint(0, 255), randint(0, 255), randint(0, 255))
#     for _ in range(i):
#         timmy_the_turtle.width(10)
#         timmy_the_turtle.speed(8)
#         timmy_the_turtle.color()
#         timmy_the_turtle.forward(100)
#         timmy_the_turtle.right(angle)


while True:
    movement = ["forward", "backward", "right", "left"]
    direction = [0, 90, 180, 270]
    print(movement)
    timmy_the_turtle.speed(0)
    for _ in range(200):
        timmy_the_turtle.width(5)
        timmy_the_turtle.color(randint(0, 255), randint(0, 255), randint(0, 255))
        timmy_the_turtle.forward(randint(1, 100))
        timmy_the_turtle.setheading(random.choice(direction))
# timmy_the_turtle.speed(0)
# timmy_the_turtle.width(5)


# def draw_spirograph(size):
#     for _ in range(360 // 10):
#         timmy_the_turtle.color(randint(0, 255), randint(0, 255), randint(0, 255))
#         timmy_the_turtle.circle(100.0)
#         timmy_the_turtle.setheading(timmy_the_turtle.heading() + 10)


draw_spirograph(1)

screen = Screen()
screen.exitonclick()
