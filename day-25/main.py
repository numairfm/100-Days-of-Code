import turtle as t

import pandas as pd

CSV = "50_states.csv"
df = pd.read_csv(CSV)
all_states = df.state.to_list()
# print(df)

screen = t.Screen()
screen.title("U.S. States Knowledge Game")

image = "blank_states_img.gif"
screen.addshape(image)

t.shape(image)


def write_state(state, x, y):
    obj = t.Turtle()
    obj.hideturtle()
    obj.penup()

    obj.goto(x, y)
    obj.write(state)


# for i in range(len(df)):
#     state = df["state"][i]
#     x = df["x"][i]
#     y = df["y"][i]

#     write_state(state, x, y)
save = "guessed_states.csv"
try:
    saved_data = pd.read_csv(save)
except FileNotFoundError:
    temp = pd.DataFrame(["0"])
    temp.to_csv(save)
    saved_data = pd.read_csv(save)

guessed_states = []

if not saved_data.empty and str(saved_data["0"].iloc[0]) != "0":
    print("exists")
    for data in saved_data["0"]:
        if data in all_states:
            guessed_states.append(data)
            state_data = df[df.state == data]
            x = int(state_data.x.item())
            y = int(state_data.y.item())
            write_state(data, x, y)
else:
    print("no saved progress or empty")

while len(guessed_states) < 50:
    answer_screen = screen.textinput(
        title=f"{len(guessed_states)}/50 States Guessed", prompt="Name a State.."
    )
    answer = str(answer_screen).title()
    print(answer)
    if answer in all_states:
        if answer not in guessed_states:
            guessed_states.append(answer)
            state_data = df[df.state == answer]
            x = int(state_data.x.item())
            y = int(state_data.y.item())
            write_state(answer, x, y)
    elif answer.lower() == "none" or answer == "":
        running = False
        break

if len(guessed_states) >= 50:
    text0 = "You win!!"
    end = t.Turtle()
    end.hideturtle()
    end.penup()
    end.goto(-50 - len(text0) * 9, 0)
    end.write(text0, font=("Arial", 50, "normal"))
    answer = screen.textinput(
        text0, "Reset Progress? Type 'YES' or anything else to ignore"
    )
    answer = str(answer)
    if answer == "YES":
        new_data = pd.DataFrame(["0"])
        new_data.to_csv(save)
else:
    if len(guessed_states) == 0:
        new_data = pd.DataFrame(["0"])
    else:
        new_data = pd.DataFrame(guessed_states)
    new_data.to_csv(save)
