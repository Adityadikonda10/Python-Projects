from turtle import Screen
import time
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
# if ball.distance(r_paddle) > 50 and ball.xcor() > 340 or ball.distance(l_paddle) > 50 and ball.xcor() < -340:
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("The Pong Game")
screen.listen()

r_paddle = Paddle((370, 0))
l_paddle = Paddle((-370, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle .go_down, "s")


game_is_on = True
while game_is_on:
    ball.move()
    # detection of collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #  detection of collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 340 or ball.distance(l_paddle) < 50 and ball.xcor()< -340:
        ball.bounce_x()
        ball.speed_up()

    # detection of miss
    if ball.xcor() > 380:
        ball.refresh()
        scoreboard.l_point()


    if ball.xcor() < -380:
        ball.refresh()
        scoreboard.r_point()


    screen.update()
    time.sleep(0.1)

    game_is_on = True

screen.exitonclick()
