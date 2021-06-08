from tkinter import *
import random
from tkinter.font import BOLD

root=Tk()
root.geometry("800x500")
root.title(" Dice Game")
root.minsize(800,200)
f1=LabelFrame(border=0,padx=30)
f1.pack(side="left")

f2=LabelFrame(border=0,padx=30)
f2.pack(side="right")

l=Label(root,text="LET'S PLAY",font=("helvantica",25),foreground="black")
l.pack()

dl=Label(root,font=("halvetica",200,BOLD),fg="red")
d2=Label(root,font=("halvetica",200,BOLD),fg="blue")

def rolldice():
    faces=['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685']
    faces2=['\u2680','\u2685']
    c=0
    chance=random.choice(faces)
    if(c==6):
        chance=random.choice(faces2)
        c=0
    else:
        if(chance=='\u2685'):
            c=0
        else:
            c=c+1   
    
    return chance

def playleft():
    dl.configure(text=rolldice())
    dl.pack(side="left")

def playright():
    d2.configure(text=rolldice())
    d2.pack(side="right")    

b1=Button(f1,text="PLAYER 1",font=("arial",20,"bold"),bg="sky blue",command=playleft)
b1.pack()

b2=Button(f2,text="PLAYER 2",font=("arial",20,"bold"),bg="orange",command=playright)
b2.pack()

root.mainloop()