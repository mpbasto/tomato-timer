from tkinter import *
import math


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#ee5c42"
GREEN = "#198d19"
YELLOW = "#FFE3A9"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
rounds = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global rounds
    window.after_cancel(timer)
    canvas.itemconfig(timer_txt, text='00:00')
    title_lbl.config(text='Get Ready', fg=GREEN)
    check.config(text='')
    rounds = 0
    

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global rounds
    rounds += 1

    work_section = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60

    if rounds % 8 == 0:
        title_lbl.config(text='LONG BREAK !', fg=RED)
        countdown(long_break)
    elif rounds % 2 == 0:
        title_lbl.config(text='SHORT BREAK', fg=PINK)
        countdown(short_break)
    else:
        title_lbl.config(text='WORK', fg=GREEN)
        countdown(work_section)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(number):
    count_min = math.floor(number / 60)
    count_sec = number % 60
    if count_sec < 10:
        count_sec = f'0{count_sec}'

    canvas.itemconfig(timer_txt, text=f'{count_min}:{count_sec}')
    if number > 0:
        global timer
        timer = window.after(1000, countdown, number - 1)
    else:
        start_timer()
        marks = ''
        work_sessions = math.floor(rounds/2)
        for _ in range(work_sessions):
            marks += '✅'
        check.config(text=marks)




# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=10, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomate_img = PhotoImage(file='./assets/tomato.png')
canvas.create_image(100, 112, image=tomate_img)
timer_txt= canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)


# title label
title_lbl = Label(text='Get Ready', font=(FONT_NAME, 40, 'bold'), fg=GREEN, bg=YELLOW)
title_lbl.grid(column=1, row=0)
title_lbl.config(pady=30)

# start button & label
start_btn = Button(text=' ▶︎ ', font=(FONT_NAME, 20), highlightthickness=0, width=2, bg=YELLOW, borderwidth=0, command=start_timer)
start_btn.grid(column=0, row=3)
start_label = Label(text='Start', font=(FONT_NAME, 18, 'bold'), bg=YELLOW, fg=GREEN)
start_label.grid(column=0, row=2)

# reset button & label
reset_btn = Button(text=' ◼︎ ', font=(FONT_NAME, 20), highlightthickness=0, width=2, bg=YELLOW, borderwidth=0, command=reset_timer)
reset_btn.grid(column=2, row=3)
reset_label = Label(text='Reset', font=(FONT_NAME, 18, 'bold'), bg=YELLOW, fg=RED)
reset_label.grid(column=2, row=2)

# check mark
check = Label(bg=YELLOW)
check.grid(column=1, row=3)











window.mainloop()