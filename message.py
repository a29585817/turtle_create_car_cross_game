from turtle import Turtle

font =("Courier", 24, "normal")

class Message(Turtle):
    def __init__(self):
        self.x = 1
        super().__init__()
        self.hideturtle()
        self.color("black")
        self.penup()
        self.goto(-250, 270)
        self.update_scoreboard()
    def update_scoreboard(self):
        self.write(arg=f"Level :{self.x}", move=False, align="left"
                   , font=font)

    def next(self):
        self.clear()
        self.goto(-250, 270)
        self.x += 1
        self.update_scoreboard()

    def win(self):
        self.goto(0, 0)
        self.write(arg="You win", move=False, align="center"
                   , font=font)

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="Game over", move=False, align="center"
                   , font=font)