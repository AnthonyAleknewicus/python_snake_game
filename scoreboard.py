from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 24, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(x=0, y=260)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"SCORE: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(x=0, y=0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.clear()
        self.score += 1
        self.goto(x=0, y=260)
        self.update_scoreboard()