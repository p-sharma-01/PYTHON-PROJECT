from turtle import Turtle, Screen
from create_paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time
screen=Screen()
screen.bgcolor("black")
screen.setup(height=600,width=800)
screen.title("Pong")
screen.tracer(0)
screen.listen()
# paddle=Turtle()
# paddle.shapesize(stretch_wid=1,stretch_len=750)
# paddle.goto(0,-280)
r_paddle=Paddle((350,0))
l_paddle=Paddle((-350,0))
ball=Ball()
scoreboard=ScoreBoard()
screen.onkey(r_paddle.move_up,"Up")
screen.onkey(r_paddle.move_down,"Down")
screen.onkey(l_paddle.move_up,"e")
screen.onkey(l_paddle.move_down,"x")


is_game_on=True
while is_game_on:
    time.sleep(ball.speed)
    screen.update()
    ball.move()
    # Detect Collision with wall
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()
    #Detect Collision with Paddle
    if (ball.distance(r_paddle.paddle)<50 and ball.xcor()>320) or (ball.distance(l_paddle.paddle)<50 and ball.xcor()<-320):
        ball.bounce_x()
    if ball.xcor()>380 :
        ball.reset_position()
        scoreboard.l_point()
        scoreboard.update()
    if ball.xcor()<-380:
        ball.reset_position()
        scoreboard.r_point()
        scoreboard.update()

screen.exitonclick()
