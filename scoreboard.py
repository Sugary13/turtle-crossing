from turtle import Turtle
FONT = ("Courier", 24, "normal")
POSITION = (-200, 260)


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(POSITION)
        self.level = 1
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def draw_level(self):
        self.clear()
        self.goto(POSITION)
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def update_scoreboard(self):
        self.level += 1
        self.draw_level()

    def game_over(self):
        self.goto(0, 0)
        self.color("red")
        self.write(f"GAME OVER.", align="center", font=FONT)

    def restart_text(self):
        self.goto(0, -30)
        self.write("Press 'r' to restart.", align="center", font=FONT)
