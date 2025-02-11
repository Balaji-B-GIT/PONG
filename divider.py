from turtle import Turtle
class Divider():
    def __init__(self):
        for pos in range(1, 580, 20):
            self.div = Turtle("square")
            self.div.color("white")
            self.div.setheading(90)
            self.div.shapesize(stretch_wid=0.2, stretch_len=0.5)
            self.div.penup()
            self.div.goto(0, -280 + pos)

