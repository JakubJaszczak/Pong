from turtle import Turtle


class Ball(Turtle):

	def __init__(self):
		super().__init__()
		self.penup()
		self.speed(1)
		self.shape("circle")
		self.color("white")
		self.setheading(45)
		self.velocity = 15

	def move(self):
		self.forward(self.velocity)
		#self.goto(self.xcor()+10,self.ycor()+10)

	def bounce(self):
		current_heading = self.heading()
		self.setheading(current_heading - 90)

	def restart(self):
		self.goto(0, 0)
		self.velocity = 15
