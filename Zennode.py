from tkinter import *
import random

root = Tk()
s = 0
vic = 'Congratulations'
def rand(ch):
    c = random.randint(1,6)
    global s, vic
    s += c
    t1.set(str(c))
    if s==100:
        t2.set(str(vic))
    elif s%7== 0 :
        s = 0
        t2.set(int(s))
    else :
        t2.set(int(s))
t1=StringVar()
t2=StringVar()
t2.set(int(s))
m1 = Label(root, text = 'Random Number: ')
m2 = Label(root, text = 'Your Account: ')
e1=Entry(root,textvariable=t1)
e2=Entry(root,textvariable=t2)
b1 = Button(root, text='Roll the Dice', command=lambda: rand('"Roll the dice'))
m1.grid(row=0,column=0)
m2.grid(row=1,column=0)
e1.grid(row=0,column=1,columnspan=2)
e2.grid(row=1,column=1,columnspan=2)
b1.grid(row=2,column=1)
root.mainloop()