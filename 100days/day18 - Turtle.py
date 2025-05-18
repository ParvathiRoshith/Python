'''
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
    
#random color for random walk
import turtle as t
tim = t.Turtle()
t.colormode(255)    #range 0 to *cmode* here cmode=255
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r,g,b)
directions=[0, 90, 180, 270] 
for i in range(200):
    timmy_the_turtle.color(random_color)
    timmy_the_turtle.forward(30)
    timmy_the_turtle.setheading(random.choice(directions))

#Spirograph
timmy_the_turtle.speed("fastest")
def draw_spirograph(num_of_gaps):
    total_circles = int(360/num_of_gaps)
    for i in range(total_circles):
        timmy_the_turtle.color(random_color)
        timmy_the_turtle.circle(100)
        current_pos = timmy_the_turtle.heading()
        timmy_the_turtle.setheading(current_pos+num_of_gaps)
draw_spirograph(5)

screen=Screen()
screen.exitonclick()
'''

#Hirst Painting Project 1
import colorgram
colour_extract = colorgram.extract("image.jpg",30)
colour_list=[]
for colour in colour_extract:
    r = colour.rgb.r
    g = colour.rgb.g
    b = colour.rgb.b
    new_colour = (r,g,b)
    colour_list.append(new_colour)

#Hirst Painting Project 2
import turtle as t
import random as r
tom=t.Turtle()
tom.hideturtle()
tom.setheading(225)  #moving starting point from middle to somewhere down
tom.forward(300)
tom.setheading(0)
tom.penup()
num_of_dots=100
for i in range(1,num_of_dots+1):
    tom.dot(10, r.choice(colour_list))
    tom.forward(50)
    if i % 10 ==0:
        tom.setheading(90)
        tom.forward(50)
        tom.setheading(180)
        tom.speed("fastest")
        tom.forward(50*10)
        tom.setheading(0)
screen=t.Screen()
screen.exitonclick()