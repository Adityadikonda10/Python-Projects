from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 10, "normal")

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.state_count = 0
        self.hideturtle()
        self.penup()

    def mark_on_map(self, state, xcor, ycor):
        self.goto(xcor, ycor)
        self.write(state, align=ALIGNMENT, font=FONT)


