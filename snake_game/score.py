from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 20, 'normal')
class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("gray")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.goto(0,270)
        self.score = 0
        self.write(f"Score: {self.score}", False, align=ALIGNMENT, font=FONT)

    def refresh(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", False, align=ALIGNMENT, font=FONT)