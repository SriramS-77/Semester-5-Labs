from tkinter import *
from random import randint
from time import sleep

top = Tk()
top.title("Bubble Sort Visualization")

lbl = Label(top, width=40)
lbl.config(text="")
lbl.pack(pady=10)

Lb1 = Listbox(top, width=40, height=10)
Lb1.pack(pady=5, padx=10)

lst = [23, 35, 4, 53, 1, 77, 9, 4, 0, 33]
for i in lst:
    Lb1.insert(END, i)

def pack(lst):
    for i in range(len(lst)):
        Lb1.insert(i+1, lst[i])

def press_btn(cur_lst):
    # cur_lst = list(Lb1.get(0, END))
    # cur_lst = lst.copy()
    n = len(cur_lst)
    
    for i in range(n-1):
        lbl.config(text=f"Step: {i+1}")
        for j in range(n-1-i):
            if cur_lst[j] > cur_lst[j+1]:
                cur_lst[j], cur_lst[j+1] = cur_lst[j+1], cur_lst[j]
                Lb1.delete(0, END)
                for k in range(len(cur_lst)):                    
                    Lb1.insert(END, lst[k])
                print(cur_lst)
                print(list(Lb1.get(0, END)))
                top.update_idletasks()
            top.after(500)
    lbl.config(text="Done!")
    return

btn = Button(top, cnf={"text": "Sort the list", "command": lambda: press_btn(lst)})
btn.pack(pady=5, padx=10)

#press_btn(lst)

top.mainloop()
