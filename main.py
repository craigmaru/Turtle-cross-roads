import time
from turtle import Turtle
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

magic = Player()  # making the player
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(magic.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    for car in car_manager.all_cars:
        if car.distance(magic) < 20:
            scoreboard.game_over()
            game_is_on = False

    if magic.on_edge():
        magic.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()
        scoreboard.update_level()

screen.exitonclick()
