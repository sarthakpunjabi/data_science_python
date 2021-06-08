from turtle import Turtle,Screen
import pandas as pd


cursor = Turtle()
screen = Screen()
screen.setup(width=700,height=500)
screen.title("US states recognization ")
screen.bgpic("blank_states_img.gif")


# def get_mouse_on_click(x,y):
#     print(x,y)

# screen.onscreenclick(get_mouse_on_click)
# screen.mainloop()

states = pd.read_csv("50_states.csv")
answer = screen.textinput(title="Guess the state" , prompt="what's the another state game ").capitalize()

try:
    ans = states[states.state == answer]
    
    cursor.write(f'{ans.state}',font=("Verdana",15, "normal"))
    
except:
    print("something went wrong ")




screen.exitonclick()
