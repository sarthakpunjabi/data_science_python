from turtle import Turtle,Screen
import pandas as pd

cursor = Turtle()
screen = Screen()
screen.setup(width=700,height=500)
screen.title("US states recognization ")
screen.bgpic("blank_states_img.gif")

states = pd.read_csv("50_states.csv")
count = 0

while count <= 50:
    try:
        answer = screen.textinput(title=f"{count}/50" , prompt="what's the another state game ").title()
        preans = states[states.state == answer]
        x = preans['x'].to_list()
        y = preans['y'].to_list()
        cursor.ht()
        cursor.up()
        cursor.goto(int(x[0]),int(y[0]))
        cursor.down()
        cursor.write(f'{answer}',font=("Verdana",15, "normal"))
        count +=1
        del states[states.state == answer]
        
    except:
        print(f"remaning states are {states}")
        break


screen.exitonclick()
