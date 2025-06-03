from turtle import Turtle
class Player:
    def __init__(self):
        self.t=Turtle("turtle")
        self.t.penup()
        self.t.goto(x=0,y=-280)
        self.t.setheading(90)
    def go_to_start(self):
        self.t.goto(x=0,y=-280)
    def move_up(self):
        self.x_cor=self.t.xcor()
        self.y_cor=self.t.ycor()+10
        self.t.goto(self.x_cor,self.y_cor)
    def move_right_side(self):
        self.x_cor=self.t.xcor()+10
        self.y_cor=self.t.ycor()
        self.t.goto(self.x_cor,self.y_cor)
    def move_left_side(self):
        self.x_cor=self.t.xcor()-10
        self.y_cor=self.t.ycor()
        self.t.goto(self.x_cor,self.y_cor)
    def finish_level(self):
        if self.t.ycor()>280:
            return True
        else:
            return False
    def position(self):
        return self.t.position()
    
