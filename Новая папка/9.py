from tkinter import *
root = Tk()
c = Canvas(root, width=200, height=200, bg='white')
c.pack()
cx = 0
cy = 160
cs = 23
ce = 290
c.create_polygon(100, 10, 20, 90, 180, 90, fill = 'lightblue')
c.create_rectangle(55, 90, 145, 160, fill = 'lightblue',
                   outline = 'lightblue')
for i in range (5, 200, 10):
    c.create_arc(cx + i, cy, cs + i, ce, 
             start=160, extent=-90, 
             style=ARC, outline='green', 
             width=2)
c.create_oval(200, 5, 155, 50,
        fill='orange',
        outline = 'orange')
root.mainloop()