import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

car_manager = CarManager()

player = Player()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(player.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move()

    # detect collision w cars
    for car in car_manager.all_cars:
        if car.distance(player) < 26:
            game_is_on = False

    if player.ycor() >= 285:
        player.start()
        scoreboard.update_score()
        car_manager.increase()
        print("You Win!")
screen.exitonclick()




