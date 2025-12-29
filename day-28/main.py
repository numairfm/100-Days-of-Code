import tkinter as tk
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg='white', highlightthickness=0)

canvas = tk.Canvas(width=200, height=224, bg='white', highlightthickness=0)
tomato_image = tk.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
canvas.create_text()

canvas.pack()


window.mainloop()