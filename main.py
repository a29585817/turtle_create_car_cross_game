from turtle import Screen
import time

from turtle_ import Turtle_
from cars import Car
from message import Message

speed = [0.1, 0.05, 0.03]
screen = Screen()
screen.setup(width=600, height=600)
screen.title("My turtle game")


screen.tracer(0)

turtle = Turtle_()
car = Car()

screen.listen()
screen.onkey(turtle.up, "Up")
screen.onkey(turtle.down, "Down")
screen.onkey(turtle.left, "Left")
screen.onkey(turtle.right, "Right")
msg = Message()



game_over = True

while game_over:
    time.sleep(0.1)
    screen.update()
    car.add_car()
    car.move()

    for x in car.cars:
        if x.distance(turtle) < 20:
            msg.game_over()
            game_over = False
    if turtle.is_finish_line():
        turtle.go_to_str()
        car.level_up()
        msg.next()




screen.exitonclick()