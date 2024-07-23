from tkinter import *
from random import randint

top = Tk()

lbl = Label(top, width=40, height=5)
lbl.config(text="Publisher Subscriber")
lbl.pack(pady=2)

Lb1 = Listbox(top, width=40, height=15)
Lb1.insert(1, 1)
Lb1.insert(2, 2)
Lb1.insert(3, 3)
Lb1.insert(4, 4)
Lb1.insert(5, 5)
Lb1.insert(6, 6)

Lb2 = Listbox(top, width=40, height=15)

Lb1.pack()
Lb2.pack()

def press_btn_add():
    to_insert = randint(1, 100)
    Lb1.insert(END, to_insert)
    lbl.config(text="Added more!")
    return

def press_btn_sub():
    if Lb1.size() == 0:
        print("Empty!!!")
        lbl.config(text="Empty! Please add more!")
        return
    pos=0
    popped = Lb1.get(pos)
    Lb1.delete(pos)
    Lb2.insert(END, popped)
    lbl.config(text=f"Passed {popped}!")
    return

add = Button(top, cnf={"text": "Get more!", "command": press_btn_add})
add.pack()

sub = Button(top, cnf={"text": "Pass it on!", "command": press_btn_sub})
sub.pack()

top.mainloop()