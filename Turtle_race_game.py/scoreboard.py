from turtle import Turtle
Font=("Courier",24,"normal")
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.level=1
        self.hideturtle()
        self.penup()
        self.goto(-280,260)
        self.write(f"Level: {self.level}", align="left", font=Font)
    def increase_score(self):
        self.level+=1
    def update_score(self):
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=Font)

