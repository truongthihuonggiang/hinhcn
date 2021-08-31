from tkinter import *
from hcn import *
tk = Tk()
cas = Canvas (tk, height = 600, width = 800)
cas.pack()
#cas.create_rectangle(10,10,200,100,outline="black",fill="green")
h1 = Hcn(50,50, 250,150)
h1.vehinh(cas)

def dichchuyen(event):
    h1.xoahinh(cas)
    if event.keysym == "Up":
        h1.dichlen()
    elif event.keysym == "Down":
        h1.dichxuong()
    elif event.keysym == "Left":
        h1.dichtrai()
    elif event.keysym == "Right":
        h1.dichphai()
    h1.vehinh(cas)

cas.bind_all('<KeyPress-Up>',dichchuyen)
cas.bind_all('<KeyPress-Down>',dichchuyen)
cas.bind_all('<KeyPress-Left>',dichchuyen)
cas.bind_all('<KeyPress-Right>',dichchuyen)


tk.mainloop()
