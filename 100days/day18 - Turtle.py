''''''
from turtle import Turtle, Screen
timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("red")
timmy_the_turtle.forward(100)
timmy_the_turtle.right(90)    # 90 degree angle to turn

#create a square
for i in range(4):                   
    timmy_the_turtle.forward(100)
    timmy_the_turtle.left(90)

#darw dashed line
for i in range(15):
    timmy_the_turtle.forward(10)
    timmy_the_turtle.penup()
    timmy_the_turtle.forward(10)
    timmy_the_turtle.pendown()

#draw triangle, square, pentagon, hexagone, heptagone, octagone, nonagon and decagon
timmy_the_turtle.forward(100)
timmy_the_turtle.right(120)


screen=Screen()
screen.exitonclick()