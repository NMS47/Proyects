from tkinter import *
import pandas
from tkinter import messagebox
import random


#-------------Functions-------------------
df = pandas
try:
    frequency_list = df.read_csv('data/Unknown_words.csv')
except FileNotFoundError:
    frequency_list = df.read_csv("data/Frequency list german.csv")

dict_wrds = frequency_list.to_dict(orient="records")
selected = {}

def next_word():
    """Selects de next word in the dictionary """
    global selected, flip_timer
    flip_timer = window.after_cancel(flip_timer)
    selected = random.choice(dict_wrds)
    current_word = selected['German']
    canvas.itemconfig(card_title, text='German', fill='black')
    canvas.itemconfig(card_word, text=current_word, fill='black')
    canvas.itemconfig(card_image, image=card_front)
    flip_timer = window.after(3000, func=change_to_back_card)

def known_word():
    """Eliminates from the list the words that you already know"""
    new_list = dict_wrds
    new_list.remove(selected)
    new_csv = df.DataFrame(new_list)
    print(new_csv)
    new_csv.to_csv('data/Unknown_words.csv', index=False)
    next_word()

def change_to_back_card():
    """Changes to the back of the card"""
    canvas.itemconfig(card_image, image=card_back)
    canvas.itemconfig(card_title, text='English', fill='white')
    canvas.itemconfig(card_word, text=selected['English'], fill='white')
#--------------Interface-------------------

BACKGROUND_COLOR = "#B1DDC6"
window = Tk()
window.title('German Flash Cards')
window.config(highlightthickness=0, bg=BACKGROUND_COLOR, padx=50, pady=50)
flip_timer = window.after(3000, func=change_to_back_card)

canvas = Canvas(highlightthickness=0, height=536, width=800, background=BACKGROUND_COLOR)
card_front = PhotoImage(file='./images/card_front.png')
card_back = PhotoImage(file='./images/card_back.png')
card_image = canvas.create_image(410, 270, image=card_front)
canvas.grid(row=0, column=0, columnspan=2)

#---------Right or Worng------------------
right_img = PhotoImage(file='./images/right.png')
right_button = Button(image=right_img, highlightthickness=0, borderwidth=0, command=known_word)
wrong_img = PhotoImage(file='./images/wrong.png')
wrong_button = Button(image=wrong_img, highlightthickness=0, borderwidth=0, command=next_word)
right_button.grid(row=1, column=1)
wrong_button.grid(row=1, column=0)

#--------Text----------------------------

card_title = canvas.create_text(400, 150, text='Click check', font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text='To Start', font=("Arial", 60, "bold"))
next_word()


window.mainloop()
