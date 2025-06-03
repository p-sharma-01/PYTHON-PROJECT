from turtle import Screen,Turtle
import time
from player import Player
from car_manager import CarManager
from scoreboard import ScoreBoard
screen=Screen()
screen.listen()
screen.title("Turtle Race Game")
screen.setup(width=600,height=600)
screen.tracer(0)
score=ScoreBoard()
play=Player()
car=CarManager()
screen.onkeypress(play.move_up,"Up")
screen.onkeypress(play.move_left_side,"Left")
screen.onkeypress(play.move_right_side,"Right")
game_is_on=True
while game_is_on:
    time.sleep(0.1)
    car.create_car()
    car.move_car()
    screen.update()
    # detect collision with cars
    for c in car.all_cars:
        if c.distance(play.position())<20:
            Turtle().hideturtle()
            Turtle().write("GAME OVER",align="center",font=("Arial",60,"normal"))
            game_is_on=False
    # Detect Successfull
    if play.finish_level():
        score.increase_score()
        score.update_score()
        play.go_to_start()
        car.level_up()
screen.exitonclick()