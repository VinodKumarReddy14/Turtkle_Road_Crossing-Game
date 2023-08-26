from turtle import Turtle
import random as r

COLORS = ["red", "blue", "green", "purple", "orange", "yellow", "violet", "indigo"]
BACKWARD_SPEED = 5

class Cars:
    def __init__(self):
        self.all_cars = []
        self.car_speed = BACKWARD_SPEED

    def create_car(self):
        rand_chance = r.randint(1, 6)
        if rand_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.penup()
            new_car.color(r.choice(COLORS))
            position = r.randint(-250, 250)
            new_car.goto(300, position)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def speedup(self):
        self.car_speed += 2



