from turtle import Turtle


class Paddle(Turtle):

	def __init__(self, position_x, position_y):
		super().__init__()
		self.penup()
		self.goto(position_x, position_y)
		self.color("white")
		self.shape("square")
		self.turtlesize(stretch_wid=5, stretch_len=1)

	def up(self):
		self.goto(self.xcor(), self.ycor()+20)

	def down(self):
		self.goto(self.xcor(), self.ycor()-20)
