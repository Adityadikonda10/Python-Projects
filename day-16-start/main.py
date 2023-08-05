from turtle import Turtle, Screen
def timmy_square():

    timmy.fd(50)
    timmy.lt(99)
    timmy.fd(50)
    timmy.lt(99)
    timmy.fd(50)
    timmy.lt(99)
    timmy.fd(50)
timmy = Turtle()
print(timmy)
timmy.shape("turtle")
# timmy.color("coral")
# # timmy.setpos(0,0)
#
# timmy_square()
timmy.color('#c588aa', '#e2ac79')
timmy.turtlesize(0.000000000000001)
timmy.begin_fill()
while True:
    timmy.speed(0.20)
    timmy.circle(100)
    # timmy_square()
    timmy.forward(200)
    timmy.left(170)
    if abs(timmy.pos()) < 1:
        break
timmy.end_fill()

#
my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()
#
# from prettytable import PrettyTable
# table = PrettyTable()
#
# table.add_column("Pokemon" ,["Pikachu", "Squrtile", "Charmendar", "Gastby"])
# table.add_column("Type", ["Electric", "Water", "Fire", "Ghost"])
# table.align = "l "
# print(table)