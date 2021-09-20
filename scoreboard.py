from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("black")
        self.penup()
        self.goto(-280, 260)
        self.hideturtle()
        self.update_level()

    def update_level(self):
        self.write(arg=f"Level: {self.level}", move=False, align="left", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", move=False, align="center", font=FONT)

    def increase_level(self):
        self.level += 1
        self.clear()
        self.update_level()
