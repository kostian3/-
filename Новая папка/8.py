from tkinter import *
from tkinter import messagebox

class Block(Tk):
    
    def __init__(self):
        super().__init__()
        frame=Frame()
        frame.pack(side=TOP)
        frame1=Frame(master=frame)
        frame1.pack(side=LEFT)
 
        frame2=Frame(master=frame)
        frame2.pack(side=LEFT)
        self.ent1=Entry(master=frame1, width=3)
        self.ent1.pack(side=TOP)
 
        self.ent2=Entry(master=frame1, width=3)
        self.ent2.pack(side=BOTTOM)
 
        Button(master=frame2,text='Изменить', command=self.change_size).pack(side=RIGHT)
 
        self.txt=Text(width=30, height=10, bg ='lightgrey')
        self.txt.pack(side=BOTTOM)
 
        self.ent1.bind('<Return>', self.change_size)
        self.ent2.bind('<Return>', self.change_size)
 
        self.txt.bind('<FocusIn>', self.change_color)
        self.txt.bind('<FocusOut>', self.change_color)
 
    def change_size(self, event=None):
        a=self.ent1.get()
        b=self.ent2.get()
        try:
            if a:
                self.txt['width']=a
            if b:
                self.txt['height']=b
        except:
            messagebox.showerror('',"Enter correct value!")
 
    def change_color(self, event):
        #print(repr(event.type))
        if event.type == '9':
            event.widget.config(bg='white')
            #или self.txt['bg']='white'
            #или self.txt.config(bg='white')
        elif event.type == '10':
            event.widget.config(bg ='lightgrey')
 
Block().mainloop()