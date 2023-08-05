import turtle as t
import random as rn
tim = t.Turtle()
tim.shape("turtle")
tim.turtlesize(0.000001)
screen = t.Screen()
COLOR = ["#FF0000","#00FF00","#0000FF","#FF00FF","#00FFFF","#FFA500","#800080","#FFFF00","#008000","#800000"]
#### HARD CODE
# for _ in range(len(COLOR)):
#     color = _
#
# def triangle():
#     tim.color(r.choice(COLOR))
#     for _ in range(3):
#         tim.forward(100)
#         tim.right(120)
#
# def square():
#     tim.color(r.choice(COLOR))
#     for _ in range(4):
#         tim.forward(100)
#         tim.right(90)
#
# def pentagon():
#     tim.color(r.choice(COLOR))
#     for _ in range(5):
#         tim.forward(100)
#         tim.right(72)
#
# def hexagon():
#     tim.color(r.choice(COLOR))
#     for _ in range(6):
#         tim.forward(100)
#         tim.right(60)
#
# def heptagon():
#     tim.color(r.choice(COLOR))
#     for _ in range(7):
#         tim.forward(100)
#         tim.right(360/7)
#
# def octagon():
#     tim.color(r.choice(COLOR))
#     for _ in range(8):
#         tim.forward(100)
#         tim.right(360/8)
#
# def nonagon():
#     tim.color(r.choice(COLOR))
#     for _ in range(9):
#         tim.forward(100)
#         tim.right(360/9)
#
# def decagon():
#     tim.color(r.choice(COLOR))
#     for _ in range(10):
#         tim.forward(100)
#         tim.right(360/10)
#
#
# triangle()
# square()
# pentagon()
# hexagon()
# heptagon()
# octagon()
# nonagon()
# decagon()

#
##### EASY CODE
# def draw_shape(sides):
#     # tim.color(r.choice(COLOR))
#     angle = 360 / sides
#     for _ in range(sides):
#         # tim.color(r.choice(COLOR))
#         tim.speed(100)
#         tim.forward(30)
#         tim.right(angle)
#
#     for _ in range(sides):
#         # tim.color(r.choice(COLOR))
#         tim.speed(100)
#         tim.forward(30)
#         tim.left(angle)
#
# for _ in range(3, 40):
#     draw_shape(_)





# RANDOM WALK CODE

t.colormode(255)

def random_color():
    r = rn.randint(0, 255)
    g = rn.randint(0, 255)
    b = rn.randint(0, 255)
    color_tuple = (r, g, b)
    return color_tuple

# num = rn.randint(0,1)
# print(num)
# tim.pensize(5)
# direction = [0, 90, 180, 270]
# for steps in range(1000):
#     tim.color(random_color())
#     # tim.color(int(random_color()[0]), int(random_color()[1]), int(random_color()[2]))
#     # num = r.randint(0, 1)
#     # print(num)
#     tim.setheading(rn.choice(direction))
#     tim.speed(15)
#     tim.forward(20)
#     # num = r.randint(0, 2)
#     # if num == 0:
#     #     tim.lt(90)
#     # elif num == 1:
#     #     tim.rt(90)
#     # else:
#     #     tim.rt(180)


# SPIROPRAPH CODE
tim.speed("fastest")
num_of_circles = int(input("Enter number of circles you want: "))
for _ in range(num_of_circles):
    tim.pensize(1)
    tim.color(random_color())
    tim.circle(130)
    tim.rt(360/num_of_circles)













screen.exitonclick()