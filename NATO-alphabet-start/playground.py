from tkinter import *

label_text = "Hello"
window = Label(text=label_text, font=('Arial', 20, 'bold'), height=10, width=30)
window.pack()


def click():
    window['text'] = input_botton.get()


botton = Button(text='Click me', command=click)
botton.pack()
input_botton = Entry(width=10)


input_botton.pack()



window.mainloop()