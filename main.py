from turtle import Turtle,Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor('black')
screen.title('My Snake Game')
screen.tracer(0)
screen.listen()
snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.onkey(snake.up,'up')
screen.onkey(snake.down,'down')
screen.onkey(snake.left,'left')
screen.onkey(snake.right,'right')

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()


    #detect collision
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_scoreboard()
    #detect with wall
    if snake.head.xcor() > 200 or snak.head.xcor() < -200 or snake.head.ycor() > 200 or snake.head.ycor() < -200:
        is_game_on = False

    #detect with tail
    for segment in snake.segments[1:]:

        if snake.head.distance(segment) < 10:
            is_game_on = False
            scoreboard.game_over()

















screen.exitonclick()