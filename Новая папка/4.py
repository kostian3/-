from tkinter import *


def open_t():
    text.delete(1.0, END)
    open_text = open(emp.get(), 'r')
    text_o =open_text.readlines()
    for item in text_o:
        text.insert(END, item)
        open_text.close()


def save():
    save_text = open(emp.get(), 'w')
    save_text.writelines(text.get(1.0, END))
    save_text.close()


root = Tk()
root.title('4')
root.resizable(False, False)
root.columnconfigure(0, minsize=90)
root.columnconfigure(1, minsize=80)
root.columnconfigure(2, minsize=70)

emp = Entry()
emp.grid(column=0, row=0, sticky='ew')

button_colour1 = Button(text="открыть", command=open_t)
button_colour1.grid(column=1, row=0, sticky='ew')
button_colour2 = Button(text="сохранить", command=save)
button_colour2.grid(column=2, row=0, sticky='ew', columnspan=3)

text = Text(width=10, wrap=WORD)
text.grid(column=0, row=1, sticky='ew', columnspan=3)

scroll1 = Scrollbar(command=text.yview)
scroll1.grid(column=4, row=1, sticky='ns')
text.config(yscrollcommand=scroll1.set)

root.mainloop()


