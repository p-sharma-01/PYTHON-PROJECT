from turtle import Turtle
class Paddle:
    def __init__(self,position):
        self.paddle=Turtle()
        self.paddle.shape("square")
        self.paddle.penup()
        self.paddle.color("white")
        self.paddle.shapesize(stretch_wid=5,stretch_len=1)
        self.paddle.goto(position)
        self.y=self.paddle.ycor()
    
    def move_up(self):
        
        self.y+=20
        self.paddle.goto(self.paddle.xcor(),self.y)
    def move_down(self):
        
        self.y-=20
        self.paddle.goto(self.paddle.xcor(),self.y)