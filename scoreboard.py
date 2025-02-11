from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score_r = 0
        self.score_l = 0
        self.display_score()

    def increase_score_r(self):
        self.clear()
        self.score_r += 1
        self.display_score()

    def increase_score_l(self):
        self.clear()
        self.score_l += 1
        self.display_score()

    def display_score(self):
        self.goto(100, 230)
        self.write(arg=f"{self.score_r} ", align="center", font=("courier", 50, "normal"))
        self.goto(-70, 230)
        self.write(arg=f"{self.score_l} ", align="center", font=("courier", 50, "normal"))
