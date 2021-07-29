from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
star_moving = 5
add_speeds = 10


class Car:
    def __init__(self):
        self.cars = []
        self.cars_speed = star_moving

    def move(self):
        for car in self.cars:
            car.backward(star_moving)

    def add_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            random_y = random.randint(-250, 250)
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.goto(300, random_y)
            self.cars.append(new_car)

    def level_up(self):
        self.cars_speed += add_speeds