from tkinter import *
 
 
class Frame(Tk):
 
    def __init__(self):
        super().__init__()
        self.title('tk')
        self.geometry("180x90")
 
        self.lbl = Label(text="", width=1)
        self.e1 = Entry(width=1, justify=CENTER)
        self.lbl.grid(row=0, column=0, columnspan=7, sticky=W+E)
        self.e1.grid(row=1, column=0, columnspan=7, sticky=W+E)
        
 
        dct = {'#ff0000': 'Красный',
               '#ff7d00': 'Оранжевый',
               '#ffff00': 'Желтый',
               '#00ff00': 'Зеленый',
               '#007dff': 'Голубой',
               '#0000ff': 'Синий',
               '#7d00ff': 'Фиолетовый'}
 
        for i, colour in enumerate(dct.keys()):
            func = lambda c=colour, ruc=dct[colour]: self.onclick(c, ruc)
            b = Button(text='', command=func, bg=colour, width=2, height=1)
            b.grid(row=2, column=i, padx=0, pady=0, sticky=W)

    def onclick(self, colour, ru_colour):
        self.e1.delete(0, END)
        self.e1.insert(0, colour)
        self.lbl['text'] = ru_colour
 
 
if __name__ == '__main__':
    root = Frame()
    root.mainloop()