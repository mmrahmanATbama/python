import random
import turtle as T
# The following extracted the colors
from colorgram import extract

colors = extract("image.jpg", 10000)
color_list =[]
for i in range(len(colors)):
    rgb_value = (colors[i].rgb.r, colors[i].rgb.g, colors[i].rgb.b)
    color_list.append(rgb_value)

# color_list = [(245, 243, 238), (246, 242, 244), (202, 164, 110), (240, 245, 241), (236, 239, 243),
#               (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20),
#               (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149),
#               (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77),
#               (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19),
#               (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102),
#               (66, 64, 60), (219, 178, 183), (178, 198, 202), (112, 139, 141), (254, 194, 0)]

# Turtle draw 10 X 10, each dot size 20, and 50 paces away
T.colormode(255)
paint = T.Turtle()
paint.speed("fastest")
paint.penup()
paint.hideturtle()
paint.setheading(225)
paint.forward(260)
paint.setheading(0)
for dot_count in range(1, 101):
    paint.dot(20, random.choice(color_list))
    paint.penup()
    paint.forward(50)

    if dot_count % 10 == 0:
        paint.setheading(90)
        paint.forward(50)
        paint.setheading(180)
        paint.forward(500)
        paint.setheading(0)

screen = T.Screen()
screen.screensize(10, 10)



screen.exitonclick()
