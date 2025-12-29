import tkinter as tk
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25 * 60
SHORT_BREAK_MIN = 5 * 60
LONG_BREAK_MIN = 20 * 60

# WORK_MIN = 2
# SHORT_BREAK_MIN = 2
# LONG_BREAK_MIN = 2

reps = 0
work_sessions_complete = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 

def stop_timer():
    global timer
    global reps
    global work_sessions_complete
    
    window.after_cancel(timer)
    
    reps = 0
    work_sessions_complete = 0
    title_label.config(text="Timer", fg=GREEN)
    check_label.config(text="")
    canvas.itemconfig(timer_text, text="00:00")

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    global work_sessions_complete
    reps += 1
    
    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN)
        title_label.config(text="Break", fg=RED)
        work_sessions_complete += 1
        check_label.config(text="✔"*work_sessions_complete)
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN)
        title_label.config(text="Break", fg=PINK)
        work_sessions_complete += 1
        check_label.config(text="✔"*work_sessions_complete)
    else:
        count_down(WORK_MIN)
        title_label.config(text="Work", fg=GREEN)
        
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    minutes = count // 60
    seconds = count % 60
    
    if seconds < 10:
        seconds = f"0{seconds}"
    
    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
window.title('Pomodoro')
window.config(padx=125, pady=50, bg=YELLOW, highlightthickness=0)
window.minsize(560, 450)
window.maxsize(560, 450)


title_label = tk.Label(text="Timer", font=(FONT_NAME, 35, "bold"), bg=YELLOW, fg=GREEN)
title_label.grid(column=1, row=0)

check_label = tk.Label(font=(FONT_NAME, 20, "bold"), bg=YELLOW, fg=GREEN)
check_label.grid(column=1, row=3)

canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato = tk.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato)
timer_text = canvas.create_text(100, 140, text="00:00", fill="white", font=(FONT_NAME, 28, "bold"))

start_button = tk.Button(text="Start", background="white", command=start_timer)
start_button.grid(column=0, row=2)
reset_button = tk.Button(text="Reset", background="white", command=stop_timer)
reset_button.grid(column=2, row=2)



canvas.grid(column=1, row=1)


window.mainloop()