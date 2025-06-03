from turtle import  Screen
import time
from snake1 import Snake
from food import Food
from score_board import ScoreBoard

screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
snake=Snake()
food=Food()
p=screen.textinput("Medium of Game","Easy / Medium / Hard")
ScoreBoard=ScoreBoard()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.right,"Right")
screen.onkey(snake.left,"Left")
Speed=0.4
if p.lower()=="easy":
    Speed=0.4
elif p.lower()=="medium":
    Speed=0.2
elif p.lower()=="hard":
    Speed=0.1
is_game_on=True
while is_game_on:
    screen.update()
    time.sleep(Speed)  
    snake.move()
    # detect collision with the food
    if snake.head.distance(food)<15:
        food.refresh()
        snake.extend()
        ScoreBoard.increase_score()
    # detect collision with the walls
    if snake.head.xcor()>290 or snake.head.xcor()<-290 or snake.head.ycor()>290 or snake.head.ycor()<-290:
        ScoreBoard.reset_scoreboard()
        snake.reset()
    #detect collision with the tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment)<10:
            ScoreBoard.reset_scoreboard()
            snake.reset()
           
            
screen.exitonclick()