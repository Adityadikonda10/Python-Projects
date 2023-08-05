from turtle import Turtle, Screen
import random


def draw_track():
    # track = Turtle(shape = "turtle")
    t = Turtle(shape="turtle")
    y_co =-screen.window_height() * 0.2 + 20
    x_co= -screen.window_width()/ 2 + 20
    fd_ln = screen.window_width() * 0.4
    fd_ln2 = screen.window_width() / 2 - 20
    for track in range(0, 6):
        t.penup()
        t.setposition( x_co, int(y_co))
        t.pendown()
        y_co += 40
        t.fd(fd_ln)
        fd_ln-=40
        t.lt(90)
        t.fd(50)
        t.rt(90)
        t.fd(fd_ln2)
        fd_ln2 += 40
    # y_co += 50
    # track.setpos(x= -screen.window_width()/2+20, y= y_co)
    #
    # track.fd(screen.window_width()* 0.4)
    # track.lt()
    # track.fd(50)
    # track.rt()
    # track.fd(screen.window_width()/2-20)



colors = ["black", "blue", "red", "green", "yellow", "purple", ]
screen = Screen()
screen.setup(width=1000, height=400)
draw_track()
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
