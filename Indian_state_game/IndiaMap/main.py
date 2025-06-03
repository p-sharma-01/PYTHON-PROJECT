import turtle
import pandas
screen=turtle.Screen()
screen.title("Indian States")
screen.addshape("./Indian_state_game/IndiaMap/India-Map.gif")
turtle.shape("./Indian_state_game/IndiaMap/India-Map.gif")

# def get_mouse_click_cor(x,y):
#     print(x,y)
# turtle.onscreenclick(get_mouse_click_cor)
# turtle.mainloop()
data=pandas.read_csv("./Indian_state_game/IndiaMap/India States.csv")
all_states=data.state.to_list()
guessed_state=[]
while len(guessed_state)<28:
    i=screen.textinput(title=f"{len(guessed_state)}/28 State Correct",prompt="What is another state").title()
    if i=="Exit":
        missing_state=[new for new in all_states if new not in guessed_state]
        new_data=pandas.DataFrame(missing_state)
        new_data.to_csv=("Missing_states.csv")
        break
    if i in all_states:
        t=turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data=data[data.state==i]
        t.goto(int(state_data.x),int(state_data.y))
        t.write(i)# state_data.state
        guessed_state.append(i)

