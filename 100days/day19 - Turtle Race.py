# Etch-a-Sketch Game
from turtle import Turtle, Screen
tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(10)

def move_backward():
    tim.backward(10)

def turn_left():
    tim.left(10)

def turn_right():
    tim.right(10)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(fun=move_forward,key="w")
screen.onkey(fun=move_backward,key="s")
screen.onkey(fun=turn_left,key="a")  #anticlockwise
screen.onkey(fun=turn_right,key="d")  #clock
screen.onkey(fun=clear,key="c")  #clear

screen.exitonclick()


# Turtle race Game
from turtle import Turtle, Screen
import random
race_on=False
screen = Screen()
screen.setup(width=500,height=400)
guess = screen.textinput(title="Make your bet",prompt="Which turtle will win the race? Enter a colour: ")
colours=['purple','blue','green','yellow','orange','red']
y_position=[-70,-40,-10,20,50,80]
all_turtles=[]

for i in range(len(colours)):
    turt = Turtle(shape='turtle')
    turt.color(colours[i])
    turt.penup()
    turt.goto(x=-250,y=y_position[i])
    all_turtles.append(turt)

if guess:
    race_on = True

while race_on:
    for turtle in all_turtles:
        if turtle.xcor()>230:
            race_on=False
            win_color=turtle.pencolor()
            if win_color == guess:
                print(f"You've won! The {win_color} turtle is the winner.")
            else:
                print(f"You've lost. The {win_color} turtle is the winner.")
        distance=random.randint(0,10)
        turtle.forward(distance)

screen.exitonclick()