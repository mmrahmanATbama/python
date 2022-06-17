import turtle
from turtle import Turtle, Screen
import random


def is_race_on(done):
    is_done = False
    if done:
        is_done = True
        for i in done:
            is_done = is_done & i
    return is_done


screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet",
                            prompt="Which turtle (v,i,b,g,y,o,r) will win the race? Enter a color: ").lower()
colors = ["violet", "indigo", "blue", "green", "yellow", "orange", "red"]
completed = []
all_turtles = []
winner = []
x_cor = -235
y_cor = -150
for colored in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.speed("fastest")
    new_turtle.color(colored)
    new_turtle.penup()
    new_turtle.goto(x=x_cor, y=y_cor)
    y_cor += 50
    all_turtles.append(new_turtle)
    completed.append(False)

if user_bet:
    is_race_started = True

competitor = 0
continue_race = False

if is_race_started:
    while not continue_race:
        for turtle in all_turtles:
            num = all_turtles.index(turtle)
            if turtle.xcor() > 230 and completed[num] is False:
                winner.append(turtle.pencolor())
                completed[num] = True
                competitor += 1
                continue_race = is_race_on(completed)
            else:
                if turtle.xcor() > 230:
                    continue
                else:
                    random_distance = random.randint(0, 5)
                    turtle.forward(random_distance)

print("Final Result:")
for index in range(len(winner)):
    print(f"\t{index + 1}: {winner[index]}")

if winner[0] == user_bet:
    print(f"You've won! The {winner[0]} turtle is the winner!")
else:
    print(f"You've lost! The {winner[0]} turtle is the winner!")
screen.exitonclick()
