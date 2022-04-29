from tkinter import *

persons = {
    'Кеша': '+4908453325',
    'Вася': '+2908445339',
    'Миша': '+1934453325',
    'Кирилл': '+2934453465',
    'Денис': '+6954233644'
}

def get_info():
    label.config(text=persons[var.get()])

root = Tk()
root.title('Информация о сотруднике')
root.resizable(height=False, width=False)

f_left = Frame(root)
f_left.pack(side=LEFT)

label = Label(root, justify='center', width=40, text='Выберите сотрудника', font=18)
label.pack(side=LEFT, expand=True)

var = StringVar()

for name in persons.keys():
    Radiobutton(f_left, width=20, font = 20, text=name, indicatoron=0, variable=var,
        value=name, command=get_info).pack(side=TOP)

root.mainloop()