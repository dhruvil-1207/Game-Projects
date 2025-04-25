from turtle import Screen
import time
from racket import Racket
from ball import Ball
from score import Score


screen = Screen()
screen.bgcolor("black")
screen.setup(width = 800,height = 600)
screen.title("Pong Game")
screen.tracer(0)

red = Racket("red",(-385,0))
blue = Racket("blue",(378,0))
mid_line = Racket("red",(0,0)).mid_line()
ball = Ball()
score = Score()
screen.listen()
screen.onkey(red.racket_up,"w")
screen.onkey(red.racket_down,"s")
screen.onkey(blue.racket_up,"Up")
screen.onkey(blue.racket_down,"Down")

game_on = True
while game_on:
    screen.update()
    time.sleep(ball.moving_speed)
    ball.move()

    # Detect collision with ceiling and the base
    if(ball.ycor()>280 or ball.ycor()<-280 ):
        ball.bounce()

    # Detects collision with walls and resets the ball's positon
    if(ball.xcor()<-385 and (ball.distance(red)>50)):
        ball.restart()
        score.change_blue()

    elif(ball.xcor()>385 and (ball.distance(red)>50)):
        ball.restart()
        score.change_red()

    # Detect collision with rackets
    if((ball.distance(red)<50 and ball.xcor()<-365) or (ball.distance(blue)<50 and ball.xcor()>358)):
        ball.hit()

    # Whoever scores 5 points first, wins!
    if (score.blue_score == 5 or score.red_score == 5):
        game_on = False
        score.game_over()

    

    

screen.exitonclick()
