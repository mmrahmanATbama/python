from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 20, 'normal')


def get_highscore():
    with open("/Users/mmrha/Desktop/data.txt") as file:
        content = int(file.read())
    return content


def update_highscore(new_score):
    with open("/Users/mmrha/Desktop/data.txt", mode="w") as file:
        file.write(str(new_score))


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("gray")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.goto(0, 270)
        self.score = 0
        self.high_score = get_highscore()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.high_score}", False, align=ALIGNMENT, font=FONT)

    def refresh(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()

    def reset_score(self):
        if self.score > int(self.high_score):
            self.high_score = self.score
            update_highscore(self.score)

        self.score = 0
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, align=ALIGNMENT, font=FONT)
