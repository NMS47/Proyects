from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

symbols = 'ABCDEFGHIJKLMNOPQRSTRSUVWXYXZabcdefghijklmnopqrstuvwxyz`~!@#$%^&*()_-=+'
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def splitted(word):
    """
    Separates a word with commas
    :param word: The list to be splitted
    :return: a list with individual characters
    """
    output = [char for char in word]
    return output


def generate_pw():
    """Generates a secure password of 12 digits """
    entry_password.delete(0, END)
    list_of_symbols = splitted(symbols)
    password_final = ''.join([random.choice(list_of_symbols) for n in range(12)])
    entry_password.insert(END, password_final)
    pyperclip.copy(password_final)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def button_add():
    """Creates and adds to a file called 'Stored pd.txt' the website, username and pass"""
    new_website = entry_website.get()
    new_username = entry_username.get()
    new_pass = entry_password.get()
    new_data = {
        new_website: {
        'email': new_username,
        'password': new_pass,

    }
                }

    if new_website == '' or new_username == '' or new_pass == '':
        messagebox.showerror(title="Something is wrong", message='Please fill in all the fields')
    else:
        is_correct = messagebox.askokcancel(title='Is the data correct?', message=f'Web: {new_website} \n'
                                                                                  f'Username: {new_username} \n'
                                                                                  f'Password: {new_pass}')
    if is_correct:
        try:
            with open('Stored_pd.json', mode='r') as text:
                data = json.load(text)
        except FileNotFoundError:
            with open('Stored_pd.json', mode='w') as text:
                json.dump(new_data, text, indent=4)
        else:
            data.update(new_data)
            with open('Stored_pd.json', mode='w') as text:
                json.dump(data, text, indent=4)

        finally:
            entry_password.delete(0, END)
            entry_website.delete(0, END)
#---------------------------SEARCH FOR WEBSITE------------------------#


def search_web():
    """ Searches for existing website username an pass"""
    new_website = entry_website.get()
    try:
        with open('Stored_pd.json') as text:
            data = json.load(text)
            try:
                username_used = data[new_website]['email']
            except KeyError:
                messagebox.showerror('Account does not exist', 'I can\'t find any username in that page.')
            else:
                password_used = data[new_website]['password']
                messagebox.showinfo(f'Your data for {new_website}: ', f'Username: {username_used} \n'
                                                                  f'Password: {password_used}')
    except FileNotFoundError:
        messagebox.showerror('No file', 'You first have to store some data to create a file.')
#--------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title('Pass Manager')
canvas = Canvas( background='gray75', highlightthickness=0, height=300, width=300)
candado = PhotoImage(file='logo.png')
canvas.create_image(150, 120, image=candado)
window.config(highlightthickness=0, bg='gray75', padx=30, pady=20)
canvas.grid(row=0, column=1)

#------------------Website-----------------------
website = Label(text='Website:', font=('Arial', 15, 'bold'), bg='gray75', justify=LEFT, anchor='w')
website.grid(row=1, column=0)
entry_website = Entry(width=44)
entry_website.focus()
entry_website.grid(row=1, column=1, columnspan=1, padx=0)
search = Button(text='Search', command=search_web,  width=14)
search.grid(row=1, column=2, padx=0,)

#------------------Username-----------------------
username = Label(text='Username/Email:', font=('Arial', 15, 'bold'), bg='gray75', justify=LEFT)
username.grid(row=2, column=0)
entry_username = Entry(width=44,)
entry_username.insert(END, 'nicolas.salvadores93@gmail.com')
entry_username.grid(row=2, column=1, columnspan=1)

#------------------Password-----------------------
password = Label(text='Password:', font=('Arial', 15, 'bold'), bg='gray75', justify=LEFT)
password.grid(row=3, column=0)
entry_password = Entry(width=44,)
entry_password.grid(row=3, column=1)
generate = Button(text='Generate Password', command=generate_pw,)
generate.grid(row=3, column=2, padx=0)

#----------------Add Password to list------------------
add_pass = Button(text='Add', width=37, command=button_add, padx=0)
add_pass.grid(row=4, column=1, columnspan=1,)

window.mainloop()
