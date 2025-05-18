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
def shape(num_of_sides):
    angle=360/num_of_sides
    for i in range(num_of_sides):
        timmy_the_turtle.forward(100)
        timmy_the_turtle.right(angle)
colours=["red","yellow","green","blue","violet","orange","black","grey"]
import random
for i in range(3,11):
    timmy_the_turtle.color(random.sample(colours))
    shape(i)

#random walk
import random
timmy_the_turtle.speed("fastest")
timmy_the_turtle.pensize(15)
colours=["red","yellow","green","blue","violet","orange","black","grey"]
directions=[0, 90, 180, 270]  #0: east, 90: north, 180: west, 270: south
for i in range(200):
    timmy_the_turtle.color(random.choice(colours))
    timmy_the_turtle.forward(30)
    timmy_the_turtle.setheading(random.choice(directions))
    

screen=Screen()
screen.exitonclick()