from tkinter import *
root = Tk()
root.title('7')
root.geometry('350x250')

def get(event):  
    a = en_1.get()  
    print(a)  

def insert(event): 
    en_1.insert(END, ' ') 

def delete(event): 
    en_1.delete(0, END) 

en_1 = Entry(font='Hack 20')  
en_1.bind('<Return>', get)  
en_1.bind('<space>', insert) 
en_1.bind('<Button-3>', delete) 
en_1.pack()
root.mainloop()


from tkinter import *
from tkinter import messagebox