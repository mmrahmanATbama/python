# Improvement ideas:
# Color the states.
# move input screen to top left
# give user option to play different way: User clicks on a state and it the name is displayed for five seconds

import turtle
import pandas

cos_x = 0
cos_y = 0
value = ()
screen = turtle.Screen()
screen.title("U.S. States Game")

# Show images in Turtle, turtle only works with .gif
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# -----------------------------------------------------------------------
# Save for reference
# mouse click and get co-ordinates
# def get_mouse_click(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click)
# # alternative way to keep window open, needed in this case
# turtle.mainloop()
# -----------------------------------------------------------------------


data = pandas.read_csv("50_states.csv")
all_state = data.state.to_list()
guessed_state = []
remaining_state = all_state

while len(guessed_state) < 50:
    answer = screen.textinput(title=f"{len(guessed_state)}/50 States Correct",
                              prompt="What's another State's name? ").title()
    if answer == "Exit":
        missing_states = []
        for state in all_state:
            if state not in guessed_state:
                missing_states.append(state)
        break

    if answer in remaining_state:
        remaining_state.remove(answer)
        guessed_state.append(answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        # data is in csv form, location ex: with columns, 0 Alabama 139, -77
        # location.state, location.x and location.y will show the individual values.
        location = data[data.state == answer]
        # the following is redundant, left for reference, helps to familiarize with syntax
        if location.state.item().lower() == answer.lower():
            t.goto(int(location.x), int(location.y))
            # location.state shows bunch more data than just the state, so get the first item, can use 'answer' as well
            t.write(location.state.item())
        else:
            print("Incorrect State name")

missing_list = pandas.DataFrame(missing_states)
missing_list.to_csv("States_missed.csv")
