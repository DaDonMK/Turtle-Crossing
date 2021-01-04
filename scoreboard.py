from turtle import Turtle
FONT = ("Courier", 16, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.goto(-250, 270)
        self.write(f"Level:{self.score}", align="center", font=FONT)

    def update_score(self):
        self.clear()
        self.score += 1
        self.write(f"Level:{self.score}", align="center", font=FONT)
