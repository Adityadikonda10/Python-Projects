import turtle
import pandas
from player import Player

player = Player()
screen = turtle.Screen()
screen.title(" U.S. State Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)




data = pandas.read_csv("50_states.csv")

print(data)


already_answered = []


game_is_on = True

while game_is_on:
    ans_state = screen.textinput(title =f"Guess a State {player.state_count}/50", prompt="What's another State's name?").title()
    state_dataframe = data[data.state == ans_state]
    state = state_dataframe.state.to_list()
    x = state_dataframe.x.to_list()
    y = state_dataframe.y.to_list()
    if ans_state == "Exit":
        missing_states = [s for s in state if s not in already_answered] 
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states to learn.csv")
        break
    if ans_state not in state:
        pass
    else:
        if ans_state not in already_answered:

            # for i in already_answered:
            #     if i != ans_state:
            player.mark_on_map(state=ans_state, xcor=x[0], ycor=y[0])
            already_answered.append(ans_state)
            print(already_answered)
            player.state_count += 1

    if player.state_count == 50:
        game_is_on = False



screen.exitonclick()
