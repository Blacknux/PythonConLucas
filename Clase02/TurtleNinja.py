from turtle import *
color=('red', 'yellow')

a=Turtle()
#a.begin_fill()
a.screen.bgcolor("Green")
colores={0:"Red",1:"Blue",2:"Darkred",3:"Cyan",4:"White"}
a.shape("turtle")
a.pen(pensize=5)
#a.pen
for x in range(4):
    a.dot(10,colores[x])
    a.color(colores[x+1])
    a.forward(100)
    a.color(colores[x])
    a.forward(100)
    a.left(90)
    #a.circle(50, 10, 80)
    
#a.end_fill()
a.penup()
a.goto(-320, 50) 
a.begin_fill()
a.pendown()
a.color("Red")
for x in range(4,0,-1):
    a.dot(10,colores[x])
    a.color(colores[x-1])
    a.forward(100)
    a.color(colores[x])
    a.forward(100)
    a.left(90)
a.color("Yellow")
a.end_fill()
a.penup()
a.goto(-120, -150)
a.color("Red")
a.turtlesize(5,5,5)   


input("")
