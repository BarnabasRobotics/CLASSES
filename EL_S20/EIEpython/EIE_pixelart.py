import turtle

screen=turtle.Screen()
screen.setup(500,500)
screen.tracer(2)

leo=turtle.Turtle()

def poly(x,y):
    leo.begin_fill()
    for i in range(y):
        leo.forward(x)
        leo.right(360/y)
    leo.end_fill()
    return

def place(x,y):
    leo.penup()
    leo.goto(x,y)
    leo.pendown()
    return

def pencolor(c):
    if c==0:
        leo.color("black","white")
    if c==1:
        leo.color("black","black")
    if c==2:
        leo.color("black","red")
    if c==3:
        leo.color("black","blue")
    if c==4:
        leo.color("black","purple")
    if c==5:
        leo.color("black","orange")
    if c==6:
        leo.color("black","tan")
    return

def grid(Mat):
    p=len(Mat)
    s=500/p
    for j in range(p):
        for i in range(p):
            place(-250+i*s,250-j*s)
            pencolor(Mat[j][i])
            poly(s,4)
    return

cb=list()
cb.append([0,0,0,0,0,0,0,0,0,0])
cb.append([0,0,0,0,0,0,0,0,0,0])
cb.append([0,0,0,0,0,0,0,0,0,0])
cb.append([0,0,0,0,0,0,0,0,0,0])
cb.append([0,0,0,0,0,0,0,0,0,0])
cb.append([0,0,0,0,0,0,0,0,0,0])
cb.append([0,0,0,0,0,0,0,0,0,0])
cb.append([0,0,0,0,0,0,0,0,0,0])
cb.append([0,0,0,0,0,0,0,0,0,0])
cb.append([0,0,0,0,0,0,0,0,0,0])

grid(cb)