from tkinter import *

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
reps = 1
reset_clicked = False

window = Tk()
window.title("Work Scheduler")
window.config(padx=100, pady= 50, bg=YELLOW)

canvas = Canvas(width=200, height=240, bg=YELLOW, highlightthickness= 0)

def reset_timer():
    global reps, reset_clicked
    reset_clicked = True
    reps = 1
    timer_label.config(text="   Timer    ", fg = GREEN)
    

def start_timer():
    global reps, reset_clicked
    reset_clicked = False
    #print(f"{reps} reps in start timer function")
    if reps % 2 != 0:
        timer(minutes = 24, seconds = 59)
        timer_label.config(text="  Work 👨‍💻   ", fg = GREEN)
    elif reps % 4 == 0:
        timer(minutes=19, seconds= 59)
        timer_label.config(text="Big Break 🥳", fg = RED)

    elif reps % 2 == 0:
        timer(minutes= 4, seconds= 59)
        timer_label.config(text="  Break 😌  ", fg = PINK)


def timer(minutes, seconds):
    global reps, reset_clicked
    if minutes < 10:
        if seconds < 10:
            canvas.itemconfig(timer_text, text= f"0{minutes}:0{seconds}")
        else:
            canvas.itemconfig(timer_text, text= f"0{minutes}:{seconds}")
    else:
        canvas.itemconfig(timer_text, text= f"{minutes}:{seconds}")  
    if seconds > 0:
        seconds -=1
    elif seconds == 0 and minutes >= 0:
        seconds = 59
        minutes -=1 
    if minutes >= 0 and reset_clicked == False:  
       window.after(1000, timer, minutes, seconds) 
    elif reset_clicked == True:
        canvas.itemconfig(timer_text, text= "00:00")
    if minutes == -1:
        reps +=1
       # print(f"{reps} reps in timer function")
        start_timer()    

timer_label = Label(text="   Timer    ", font=(FONT_NAME, 35, "bold"), fg=GREEN, bg=YELLOW)
timer_label.grid(column=1, row=0)

tomato = PhotoImage(file="tomato.png")

canvas.create_image(100,112, image= tomato)
timer_text = canvas.create_text(100,130, text=f"00:00", fill="white", font=(FONT_NAME, 25, "bold"))
canvas.grid(column=1, row= 1)


start_button = Button(text="start", font=(FONT_NAME, 10, "bold"), command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="reset", font=(FONT_NAME, 10, "bold"), command= reset_timer)
reset_button.grid(column=2, row=2)


window.mainloop()