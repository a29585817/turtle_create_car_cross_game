from turtle import Turtle

up = 90
down = 270
right = 0
left = 180
Finish_line = 280
Start = (0, -260)

class Turtle_(Turtle):
    def __init__(self):
        super().__init__()
        self.color("purple")
        self.setheading(90)
        self.penup()
        self.shape("turtle")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.go_to_str()


    def go_to_str(self):
        self.goto(Start)

    def is_finish_line(self):
        if self.ycor() > Finish_line:
            return True
        else:
            return False

    def up(self):
        if self.heading() == up:
            self.forward(10)
        self.setheading(up)

    def down(self):
        if self.heading() == down:
            self.forward(10)
        self.setheading(down)

    def right(self):
        if self.heading() == right:
            self.forward(10)
        self.setheading(right)

    def left(self):
        if self.heading() == left:
            self.forward(10)
        self.setheading(left)

