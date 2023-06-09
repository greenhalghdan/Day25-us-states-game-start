import turtle
import pandas
screen = turtle.Screen()
screen.title("US states game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
correct_gusses = []
score = 0
STATES = 50
states = pandas.read_csv("50_states.csv")
listofstates = states["state"].to_list()

while len(correct_gusses) < 50:
    answer_state = screen.textinput(title=f"{len(correct_gusses)}/50 States Correct", prompt="enter a guess").title()
    if answer_state == "Exit":
        statestolearn = [state for state in listofstates if state not in correct_gusses]
        df = pandas.DataFrame(statestolearn, columns=['state'])
        df.to_csv("states_to_lean.csv")
        break
    if answer_state not in correct_gusses:
        correct_gusses.append(answer_state)
        if answer_state in listofstates:
            score += 1
            d = turtle.Turtle()
            d.hideturtle()
            d.penup()
            location = states[states.state == answer_state]
            d.goto(int(location.x), int(location.y))
            d.write(answer_state)
# statestolearn = []
# with open("states_to_lean.csv", "w") as new_file:
#     for state in listofstates:
#         if state not in correct_gusses:
#             statestolearn.append(state)



