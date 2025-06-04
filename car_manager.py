
from turtle import Turtle
from random import choice, randint
COLOR = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class Car(Turtle):
    def __init__(self):
        super().__init__("square")
        self.penup()
        self.color(choice(COLOR))
        self.turtlesize(stretch_wid=1, stretch_len=2)
        self.seth(180)
        self.goto(280, randint(-250, 250))

class CarManager:
    def __init__(self):
        self.all_cars = []
        self.move_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        if randint(1, 6) == 1:
            new_car = Car()
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.forward(self.move_speed)

    def level_up(self):
        self.move_speed += MOVE_INCREMENT

    def remove_offscreen_cars(self):
        self.all_cars = [car for car in self.all_cars if car.xcor() > -320]



