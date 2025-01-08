from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My snake game")

screen.tracer(0)#tracer used to turn or off the screen animation and to start again use update; tracer is used so that animation could look good

snake=Snake()
food=Food()
scoreboard=Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")


game_is_on=True
while game_is_on:
    screen.update()  # update used to give order for when to draw the screen again after stoping from screen.tracer
    #very important only update the screen when all the segments have move forward
    time.sleep(0.1)#only delay after all the segments have moved
    snake.move()

    #dect collision with food
    if snake.head.distance(food) < 15:#less than 15 food size is 20
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    #detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on=False
        scoreboard.game_over()

    #detect collision with tail
    for segment in snake.segment[1:]:#[1:] leaving the first segment
        # if segment == snake.head:#beacuse the first segment will always < than 10 to second segment
        #     pass #replaced with python slicing [1:]
        if snake.head.distance(segment) <10:#<10 means hits the body or the tail
            game_is_on=False
            scoreboard.game_over()

screen.exitonclick()