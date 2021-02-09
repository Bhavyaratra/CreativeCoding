from tkinter import *
import random, math
#from tkinter.ttk import Scale


def disp():
    print(str(angleV.get()))
    canvas.delete("all")
    drawtree(300,400,-90,9) 


window = Tk()
angleV=IntVar()
window.title('Fractal Tree')
window.geometry('600x600')
canvas= Canvas(window,width='600',height='500',bg="black")
canvas.grid(column=0,row=0,columnspan= 50)
v=10
s1= Scale(window,variable= angleV, from_=1,to= 90, orient=HORIZONTAL)
angleV.set(20)
b1= Button(window,text = 'display',command= disp,pady=2)
s1.grid(column=1,row=1)
b1.grid(column=2,row=1)
def drawtree(x1,y1,angle,depth):
    
    if(depth>0):
        x2= x1+ int(math.cos(math.radians(angle))*8*depth)
        y2= y1+ int(math.sin(math.radians(angle))*8*depth)
        canvas.create_line(x1,y1,x2,y2,fill="white",width=2)
        drawtree(x2,y2,angle-angleV.get(),depth-0.5)
        drawtree(x2,y2,angle+angleV.get(),depth-0.5)


drawtree(300,400,-90,9)    

window.mainloop()