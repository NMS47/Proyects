from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = -1
text_check = ''
my_timer = None

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    window.after_cancel(my_timer)
    global reps
    global text_check
    text_check = ''
    reps = -1
    start_timer()
    reps = -1
    text_check = ''
    timer_word.config(text='Timer', fg=GREEN)
    window.after_cancel(my_timer)

# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    global reps
    reps += 1
    if reps < 9:
        reps -= 10

    work_segs = WORK_MIN * 60
    short_break_segs = SHORT_BREAK_MIN * 60
    long_break_segs = LONG_BREAK_MIN * 60

    if reps % 2 == 0:
        timer_countdown(work_segs)
        timer_word.config(text='CODE', fg=GREEN)
        global text_check
        text_check += '✅'
        checks.config(text=text_check)
    elif reps % 5 == 0:
        timer_countdown(long_break_segs)
        timer_word.config(text='Long rest', fg=RED)
    else:
        timer_countdown(short_break_segs)
        timer_word.config(text='Short rest', fg=PINK)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def timer_countdown(count):
    minutes = math.floor(count / 60)
    seconds = count % 60
    if seconds < 10:
        seconds = str(seconds).zfill(2)
    if seconds == 0:
        seconds = "00"
    canvas.itemconfig(timer, text=f"{minutes}:{seconds}")
    if count > 0:
        global my_timer
        my_timer = window.after(1, timer_countdown, count - 1)
    else:
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title('Pomodoro')
window.config(padx=70, pady=50, bg=YELLOW, highlightthickness=0)
timer_word = Label(text='Timer', font=(FONT_NAME, 25, 'bold'), bg=YELLOW, fg=GREEN)
timer_word.grid(row=0, column=1)

start = Button(text="Start", command=start_timer)
start.grid(row=2, column=0)


reset = Button(text="Reset", command=reset_timer)
reset.grid(row=2, column=2)

checks = Label(text=text_check, font=(FONT_NAME, 15, 'bold'), fg=GREEN)
checks.grid(row=3, column=1)

canvas = Canvas(width=206, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(102, 112, image=tomato_img)
timer = canvas.create_text(100, 132, text="00:00", font=(FONT_NAME, 20, 'bold'), fill='white')

canvas.grid(row=1, column=1)


window.mainloop()
