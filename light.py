from tkinter import *
window = Tk()
window.geometry("300x300")
window.title("Hello")

CANVAS_HEIGHT = 300
CANVAS_WIDTH = 300

canvas = Canvas(window, width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
background = canvas.create_rectangle(0, 0, 300, 300, fill="white", outline = 'white')
canvas.pack()

rectangles = []
i = 0


while i*15 < CANVAS_HEIGHT:
    # left side
    r1 = canvas.create_rectangle(0,i*15,10,10+(i*15), fill="blue")

    # right side
    canvas.create_rectangle(CANVAS_HEIGHT-10,i*15,CANVAS_HEIGHT,10+(i*15), fill="blue")

    # top
    canvas.create_rectangle(i*15, 0, 10+(i*15), 10, fill="blue")

    # bottom
    canvas.create_rectangle(i*15, CANVAS_WIDTH-10, 10+(i*15), CANVAS_WIDTH, fill="blue")

    i = i + 1


def winter():
    canvas.itemconfig(background, fill="blue")
    canvas.itemconfig(r1, fill="red")
    #fill red blue green white

def spring():
    canvas.itemconfig(background, fill="pink")
    canvas.itemconfig(r1, fill="yellow")
    #fill purple yellow green pink

def summer():
    canvas.itemconfig(background, fill="red")
    #canvas.itemconfig(r1, fill="red")
    #fill yellow pink blue orange

def fall():
    canvas.itemconfig(background, fill="yellow")
    #canvas.itemconfig(r1, fill="red")
    #fill brown yellow orange red

label1=Label(window, text="Welcome", fg="blue", bg="yellow", font=("arial", 16, "bold"))
label1.place(x=100,y=25)

b1=Button(window,text="Winter",width=12,bg="blue",fg="white",command=winter)
b1.place(x=100,y=100)

b2=Button(window,text="Spring",width=12,bg="blue",fg="white",command=spring)
b2.place(x=100,y=130)

b3=Button(window,text="Summer",width=12,bg="blue",fg="white",command=summer)
b3.place(x=100,y=160)

b4=Button(window,text="Fall",width=12,bg="blue",fg="white",command=fall)
b4.place(x=100,y=190)

window.mainloop()