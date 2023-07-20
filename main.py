from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
#Starting positions of right paddle; left paddle XPOS = -XPOS
XPOS = 350
YPOS = 0

#Screen creation and setup
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

#Create left and right paddle objects
left_paddle = Paddle(-XPOS, YPOS)
right_paddle = Paddle(XPOS, YPOS)
#Creating a ball object
ball = Ball()
scoreboard = Scoreboard()
#Assigning keys to move left and right paddle
screen.listen()
screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")
screen.onkey(right_paddle.up, "i")
screen.onkey(right_paddle.down, "k")

game_is_on = True
while game_is_on:

	screen.update()
	ball.move()
	time.sleep(0.1)
	if abs(ball.ycor()) > 280:
		ball.bounce()
	#Colision with the right paddle and giving points
	if ball.distance(right_paddle) < 50 and ball.xcor() > 320:
		ball.bounce()
		ball.velocity += 2


	#Colision with the left paddle
	if ball.distance(left_paddle) < 50 and ball.xcor() < -320:
		ball.bounce()
		ball.velocity += 2

	if ball.xcor() > 350:
		scoreboard.clear()
		ball.setheading(225)
		scoreboard.left_point()
		ball.restart()

	if ball.xcor() < -350:
		ball.setheading(45)
		scoreboard.clear()
		scoreboard.right_point()
		ball.restart()


screen.exitonclick()
