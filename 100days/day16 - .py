'''import turtle
print(turtle.Turtle)'''

'''
from turtle import Turtle,Screen
timmy=Turtle()            #object is the class
print(timmy)

timmy.shape("turtle")     #object.method
timmy.color("coral")
timmy.forward(100)

my_screen=Screen()
print(my_screen.canvheight)   #object.attribute    ##attribute is nothing but variable in the class
my_screen.exitonclick()
'''
#import prettytable      #installed external library
from prettytable import PrettyTable               #prettytable->library  #PrettyTable->class
table=PrettyTable()                               #the variable, table, is the object
#print(table)
table.add_column("Pokemon Name",["Pikachu","Squirtle","Charmander"])
table.add_column("Type",["Electric","Water","Fire"])
print(table)