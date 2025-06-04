from turtle import Turtle

STARTING_POSITION = (0,-280)
MOVE_DISTANCE = 10
FINISH_LINE_y = 280

class Player(Turtle):

    def __init__(self):
        super().__init__(shape="turtle")
        self.penup()
        self.seth(90)
        self.goto(STARTING_POSITION)

    def move(self):
        self.forward(MOVE_DISTANCE)

    def finish_line(self):
        if self.ycor() > FINISH_LINE_y:
            self.goto(STARTING_POSITION)
            return True
        return False

    def player_collision(self, other_object):
        return self.distance(other_object) < 20
