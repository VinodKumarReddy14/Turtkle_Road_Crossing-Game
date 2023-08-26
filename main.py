from turtle import Screen
from tom import Tom
import time
from car import Cars
from level import Level
TIME_SLEEP = 0.1

screen = Screen()
screen.bgcolor("white")
screen.setup(width=600, height=600)
screen.title("Turtle Road Cross")

screen.tracer(0)
tom = Tom()
car = Cars()
level = Level()

screen.listen()
screen.onkey(tom.move_up, "Up")
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(TIME_SLEEP)
    car.create_car()
    car.move_cars()
    if tom.ycor() > 300:
        level.update_level()
        tom.goto(0, -280)
        car.speedup()

    for c in car.all_cars:
        if tom.distance(c) < 26:
            game_is_on = False
            level.game_over()


screen.exitonclick()
