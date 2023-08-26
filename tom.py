from turtle import Turtle


class Tom(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.goto(0, -280)
        self.setheading(self.heading() + 90)

    def move_up(self):
        self.forward(10)
