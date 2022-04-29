from tkinter import *
from tkinter.ttk import *

def toSecond():
    selectToSecond = lbox1.curselection()

    for i in selectToSecond:
        lbox2.insert(END, lbox1.get(i))

    for i in reversed(selectToSecond):
        lbox1.delete(i)


def toFirst():
    selectToFirst = lbox2.curselection()

    for i in selectToFirst:
        lbox1.insert(END, lbox2.get(i))

    for i in reversed(selectToFirst):
        lbox2.delete(i)


root = Tk()

lbox1 = Listbox(selectmode=EXTENDED)

for i in ('print','potato','demon','android','bread','carrot','bananas','apple'):
    lbox1.insert(0,i)

lbox1.pack(side=LEFT)

lbox2 = Listbox(selectmode=EXTENDED)
lbox2.pack(side=RIGHT)

f = Frame()
f.pack(side=LEFT, padx=10)
Button(f, text=">>>", command=toSecond).pack(fill=X)
Button(f, text="<<<", command=toFirst).pack(fill=X)

root.mainloop()