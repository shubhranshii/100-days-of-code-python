import turtle
import pandas
from write import Write

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
writer = Write()

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
game_is_on = True
guessed_states = []

while game_is_on:
    answer = (screen.textinput(title=f"{len(guessed_states)}/50 States", prompt="What's another state?")).title()
    for index in data.index:

        if answer == "Exit":
            states_missed = []
            for state in all_states:
                if state not in guessed_states:
                    states_missed.append(state)
            data_missed_states = pandas.DataFrame(states_missed)

        if data["state"][index] == answer:
            guessed_states.append(answer)
            writer.write_state(answer, data["x"][index], data["y"][index])

screen.exitonclick()
