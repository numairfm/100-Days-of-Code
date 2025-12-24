import time
from turtle import Screen

from car_manager import CarManager
from environment import Environment
from player import Player
from scoreboard import Scoreboard

score_board = Scoreboard()
car_manager = CarManager()
screen = Environment()
player = Player()
screen.handle_input(player)

car_manager.create_traffic()


game_is_on = True
while game_is_on:
    if player.at_finish_line(car_manager):
        score_board.increase_level()
        time.sleep(1)

    car_manager.drive_cars()
    if player.check_collision(car_manager.all_cars):
        time.sleep(1)
        game_is_on = False
        break

    car_manager.update_speed(player.level)
    time.sleep(0.01)
    screen.update()
