from turtle import Turtle
X_COR = 10
Y_COR = 10


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.setpos(0, 0)
        self.x_move = 10
        self.y_move = 10

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def speed_up(self):
        self.x_move *= 1.05
        self.y_move *= 1.05

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def refresh(self):
        self.goto(0,0)
        self.bounce_x()
        self.x_move = 10
        self.y_move = 10


