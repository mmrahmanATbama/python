from turtle import Turtle, Screen


def move_forward():
    sketch.forward(10)


def move_backward():
    sketch.backward(10)


def move_counter_clock():
    new_heading = sketch.heading() + 10
    sketch.setheading(new_heading)


def move_clockwise():
    new_heading = sketch.heading() - 10
    sketch.setheading(new_heading)


def clear_screen():
    sketch.clear()
    sketch.penup()
    sketch.home()
    sketch.pendown()


sketch = Turtle()
screen = Screen()

screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=move_counter_clock)
screen.onkey(key="d", fun=move_clockwise)
screen.onkey(key="c", fun=clear_screen)

screen.exitonclick()
