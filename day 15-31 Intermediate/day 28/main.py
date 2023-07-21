from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0.1
SHORT_BREAK_MIN = 0.1
LONG_BREAK_MIN = 20
reps=0
timer=None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    start_button.config(state="normal")
    reset_button.config(state="disabled")
    global timer,reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_countdown, text="00:00")
    timer_label.config(text="Timer",fg=GREEN)
    tick_label.config(text="")
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    start_button.config(state="disabled")
    reset_button.config(state="normal")
    global reps
    reps += 1

    work_timer=WORK_MIN *60
    short_break= SHORT_BREAK_MIN*60
    long_break=LONG_BREAK_MIN*60

    if reps%8==0:
        timer_label.config( fg=RED,text="Break")
        countdown(long_break)
    elif reps%2==0:
        timer_label.config( fg=PINK, text="Break")
        countdown(short_break)
    else:
        timer_label.config( text="Work", fg=GREEN)
        countdown(work_timer)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    minutes=math.floor(count/60)
    seconds=count%60
    if seconds<10:
        seconds=f"0{seconds}"
    canvas.itemconfig(timer_countdown, text=f"{minutes}:{seconds}")
    if count==0:
        window.bell()
        start_timer()
        global reps
        ticks=""
        work_sessions=math.floor(reps/2)
        for i in range (work_sessions):
            ticks+="✔"
        tick_label.config(text=ticks)

    if count>0:
        global timer
        timer=window.after(1000,countdown,count-1)

# ---------------------------- UI SETUP ------------------------------- #

window=Tk()
window.title("Pomodoro")
window.config(padx=100, pady=100, bg= YELLOW)

canvas= Canvas(width=200,height=224,bg=YELLOW, highlightthickness=0)
tomato_img= PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato_img)
timer_countdown=canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME, 28, "bold"))
canvas.grid(row=1,column=1)

timer_label=Label(text="Timer", bg=YELLOW, fg= GREEN,font=(FONT_NAME, 28, "bold"))
timer_label.grid(row=0,column=1)

tick_label=Label( bg=YELLOW, fg= GREEN,font=(FONT_NAME, 28, "bold"))
tick_label.grid(row=3,column=1)

start_button=Button(text="Start", bd=2,width=10, command=start_timer, state="normal")
start_button.grid(row=2,column=0)

reset_button=Button(text="Reset", bd=2,width=10, command=reset_timer, state= "disabled")
reset_button.grid(row=2,column=2)

window.mainloop()
