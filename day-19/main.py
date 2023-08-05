from turtle import Turtle, Screen
import random

# tim.color("black")
#
# tom = Turtle()
# tom.color("black")
#
# jim = Turtle()
# jim.color("black")
#
# max = Turtle()
# max.color("black")
#
# jaw = Turtle()
# jaw.color("black")
#
# can = Turtle()
# can.color("black")
#
# nim = Turtle()
# nim.color("black")
colors = ["black", "blue", "red", "green", "yellow", "purple", ]
screen = Screen()
screen.setup(width=1000, height=400)
user_bet = screen.textinput(title = "Make your bet", prompt = "Which turtle do you think will win? Enter a color: ")
# print(screen.window_width())
y= -screen.window_height() * 0.2
all_turtles = []
for index_number in range(0, 6):
    tim = Turtle(shape="turtle")
    tim.penup()
    tim.color(colors[index_number])
    y+=30
    tim.setposition(-screen.window_width()/2+20,y)
    all_turtles.append(tim)

if user_bet:
    is_race_on_= True

while is_race_on_:
    for turtle in all_turtles:
        turtle.fd(random.randint(0,10))
        if turtle.xcor() > screen.window_width()/2-20:
            is_race_on_= False
            winning_turtle = turtle.pencolor()
            if winning_turtle == user_bet:
                print(f"You've won {winning_turtle} is the winner")
            else:
                print(f"You've lost {winning_turtle} is the winner")





#
# def forwards():
#     tim.fd(10)
# def backwards():
#     tim.bk(10)
# def left():
#     tim.lt(10)
# def right():
#     tim.rt(10)
# def clear():
#     tim.clear()
#     tim.reset()
#
# screen.onkey(forwards, "w")
# screen.onkey(backwards, "s")
# screen.onkey(left, "a")
# screen.onkey(right, "d")
# screen.onkey(clear, "c")
# screen.listen()









screen.exitonclick()