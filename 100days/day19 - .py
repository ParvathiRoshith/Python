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
screen = Screen()
screen.setup(width=500,height=400)
guess = screen.textinput(title="Make your bet",prompt="Which turtle will win the race? Enter a colour: ")
colours=['purple','blue','green','yellow','orange','red']

tim = Turtle(shape='turtle')
tim.penup()
tim.goto(x=-250,y=-100)

for i in colours:
    

screen.exitonclick()