from tkinter import *

win = Tk()
win.geometry('400x200')
win.title('Выпаадающее меню')

var = StringVar(win)
var.set('Выберите Тему')

drop_down = OptionMenu(win, var, 'Тема #1', 'Тема #2', 'Тема #3', 'Тема #4')
drop_down.pack()


def ok():
    print("value is", var.get())
    var_user = var.get()
    if var_user == 'Тема #1':
        print('#1')
    win.quit()


button = Button(win, text="OK", command=ok)
button.pack()

win.mainloop()
