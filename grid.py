from tkinter import *
from vpython import *
from time import *

mRadius=.75
wallThickness=.1

root = Tk()

h = Entry(root, width=50)
h.pack()
w = Entry(root, width=50)
w.pack()
d = Entry(root, width=50)
d.pack()

def myClick():
    myLabel1 = Label(root, text=h.get())
    myLabel1.pack()
    myLabel2 = Label(root, text=w.get())
    myLabel2.pack()
    myLabel3 = Label(root, text=d.get())
    myLabel3.pack()
def drawShape():
    floor=box(pos=vector(0,-myLabel1/2,0),size=vector(myLabel2,wallThickness,myLabel3),color=color.white)
    ceiling=box(pos=vector(0,myLabel1/2,0),size=vector(myLabel2,wallThickness,myLabel3),color=color.white)
    backWall=box(pos=vector(0,0,-d/2),size=vector(myLabel2,myLabel1,wallThickness),color=color.white)
    leftWall=box(pos=vector(-myLabel2/2,0,0),size=vector(wallThickness,myLabel1,myLabel3),color=color.white)
    rightWall=box(pos=vector(myLabel2/2,0,0),size=vector(wallThickness,myLabel1,myLabel3),color=color.white)
    marble=sphere(redius=mRadius,color=color.red)
    deltaX=.1
    xPos=0
    while True:
        rate(10)
        xPos=xPos+deltaX
        if(xPos>1 or xPos<-1):
            deltaX=deltaX*(-1)
            marble.pos=vector(xPos,0,0)


myButton = Button(root, text="Enter your name",command=myClick)
myButton.pack()

myButton = Button(root, text="Enter your name",command=drawShape)
myButton.pack()




#myLabel1 = Label(root, text="Hello World")
#myLabel2 = Label(root, text="My name is Don")

#myLabel1.grid(row=0, column=0)
#myLabel2.grid(row=1, column=5)

root.mainloop()
