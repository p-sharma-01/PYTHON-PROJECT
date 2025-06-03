from turtle import Turtle 
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        with open("My_first_game/data.txt")as data:
            self.high_score=int(data.read())
        self.color("pink")
        self.penup()
        self.goto(0,270)
        self.update_score()
        self.hideturtle()
    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score} ",align="center",font=("Arial",12,"normal"))
    def reset_scoreboard(self):
        if self.score>self.high_score:
            with open("./My_first_game/data.txt",'w')as data:
               data.write(self.score)
            
        self.score=0
        self.update_score()
    def increase_score(self):
        self.score+=1
       
        self.update_score()