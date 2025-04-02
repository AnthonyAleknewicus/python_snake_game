from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0) # screen.tracer() method controls how fast the turtle's drawing updates on the screen. It’s like telling the turtle whether to show its work step-by-step or wait until it’s done



snake = Snake()
food = Food()
snake.create_snake()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 20:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()




screen.exitonclick()

# Step 01: Create a Snake Body
# Step 02: Move the Snake
# Step 03: Control the Snake
# Step 04: Detect collision with food
# Step 05: Create a scoreboard
# Step 06: Detect collision with wall
# Step 07: Detect collision with tail