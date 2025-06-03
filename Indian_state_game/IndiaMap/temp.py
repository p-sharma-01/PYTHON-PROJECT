import turtle
import pandas
screen=turtle.Screen()
screen.title("State Game")
screen.addshape("./Indian_state_game/IndiaMap/India-Map.gif")
turtle.shape("./Indian_state_game/IndiaMap/India-Map.gif")
data=pandas.read_csv("./Indian_state_game/IndiaMap/India States.csv")
all_states=data.state.to_list()
Guessed_list=[]
while len(Guessed_list)<28:
    i=screen.textinput(title=f"{len(Guessed_list)}/28 Correctly Guessed",prompt="Another state Game :").title()
    if i=="Exit":
        missed=[]
        for i in all_states:
            if i not in Guessed_list:
                missed.append(i)
        dat=pandas.DataFrame(missed)
        dat.to_csv("missed_states.csv")
        break
    if i in all_states:
        Guessed_list.append(i)
        t=turtle.Turtle()
        t.hideturtle()
        t.penup()
        s=data[data.state==i]
        t.goto(int(s.x.iloc[0]),int(s.y.iloc[0]))
        t.write(i)
