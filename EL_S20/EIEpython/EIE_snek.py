#Snake Game by Eric Lin

#Imported libraries
import turtle
from time import sleep
#############

#Setup screen
screen=turtle.Screen()
screen.setup(600,600)
screen.title("Snek Gaem")
screen.bgcolor("green")
#############

#Snek hed
hed=turtle.Turtle()
hed.penup()
hed.color("black")
hed.shape("turtle")
#############

#Variables
direction="down"
#############

#Functions
def move():
    if direction=="right":
        hed.seth(0)
        hed.setx(hed.xcor()+20)
    if direction=="left":
        hed.seth(180)
        hed.setx(hed.xcor()-20)
    if direction=="up":
        hed.seth(90)
        hed.sety(hed.ycor()+20)
    if direction=="down":
        hed.seth(270)
        hed.sety(hed.ycor()-20)
#############

#Main game loop
while True:
    direction="right"
    move()
    sleep(0.15)
    direction="down"
    move()
    sleep(0.15)
#############