from tkinter import *
from tkinter import messagebox as mb

root = Tk()


def btn_click():
    login = login_input.get()
    password = pass_field.get()

    info_str = f'Данные: {str(login)}, {str(password)}'

    if login and password != '':
        mb.showinfo(title='Название', message=info_str)
    else:
        mb.showerror(title='', message='Error always!')


root.title = 'Hello tkinter!'
root.geometry('720x480')
root['bg'] = 'tomato'

canvas = Canvas(root, height=300, width=250)
canvas.pack()

frame = Frame(root, bg='#eee')
frame.place(relx=0.15, rely=0.15, relwidth=0.7, relheight=0.7)

title = Label(frame, text='Текст подсказка', bg='gray', font=40)
title.pack()

login_input = Entry(frame, bg='white')
login_input.pack()

pass_field = Entry(frame, bg='white', show='*')
pass_field.pack()

btn = Button(frame, text='Кнопка', bg='yellow', command=btn_click)
btn.pack()

root.mainloop()
