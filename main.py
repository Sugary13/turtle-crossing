import time
import os
from player import Player
from turtle import Screen
from scoreboard import Scoreboard
from car_manager import CarManager

screen = Screen()

screen.setup(width=600, height=600)
screen.title("Turtle Crossing")
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
new_car = CarManager()

game_is_on = True

def restart():
    if not game_is_on:
        screen.bye()
        os.system("python main.py")

screen.listen()
screen.onkeypress(player.move, "Up")
screen.onkey(restart, "r")



while game_is_on:
    time.sleep(0.1)
    new_car.create_car()
    new_car.move_cars()
    screen.update()
    new_car.remove_offscreen_cars()
    if player.finish_line():
        scoreboard.update_scoreboard()
        new_car.level_up()
    for car in new_car.all_cars:
        if player.player_collision(car):
            game_is_on = False
            scoreboard.game_over()



screen.exitonclick()