from turtle import Turtle
import random
colors=["red","orange","yellow","green","blue","purple"]

class CarManager():
    def __init__(self):
        self.all_cars=[]
        self.starting_move_distance=5
    def create_car(self):
        random_number=random.randint(1,6)
        if random_number==1 :
            new_car=Turtle("square")
            new_car.shapesize(stretch_wid=1,stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(colors))
            random_y=random.randint(-250,250)
            new_car.goto(300,random_y)
            self.all_cars.append(new_car)
    def move_car(self):
        for i in self.all_cars:
            i.penup()
            x_cor=i.xcor()-self.starting_move_distance
            i.goto(x_cor,i.ycor())
    def level_up(self):
        self.starting_move_distance+=1


