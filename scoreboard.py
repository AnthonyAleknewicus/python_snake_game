from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(x=0, y=260)
        self.write(f"SCORE: {self.score}", align="center", font=('Arial', 20, 'normal'))

    def increase_score(self):
        self.clear()
        self.score += 1
        self.goto(x=0, y=260)
        self.write(f"SCORE: {self.score}", align="center", font=('Arial', 20, 'normal'))