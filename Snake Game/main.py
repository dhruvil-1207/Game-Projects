from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width = 600,height = 600)
screen.title("Snake Game")
screen.tracer(0)


snake = Snake()
food  = Food()
score = Score()
screen.listen()
screen.onkey(snake.up,"w")
screen.onkey(snake.down,"s")
screen.onkey(snake.left,"a")
screen.onkey(snake.right,"d")
game_on = True
while game_on:
    screen.update()     
    time.sleep(0.1)
    snake.move()
    if(int(snake.head.distance(food)) <17):
        food.gen_new()
        snake.extend()
        score.change_score()
    if(snake.head.xcor() > 285 or snake.head.xcor() < -285 or snake.head.ycor() >  285 or snake.head.ycor() < -285):
        game_on = False
        score.game_over()

    for square in snake.squares[1:]:
        if(snake.head.distance(square)<10):
            game_on = False
            score.game_over()
    


        

screen.exitonclick()

