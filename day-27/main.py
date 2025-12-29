import tkinter as tk

window = tk.Tk()
window.title("My Window")

resolution = (250, 125)
window.minsize(*resolution)
window.maxsize(*resolution)
window.config(padx=30, pady=30)

# ---- Labels ---- #

label0 = tk.Label(text="Miles")
label0.grid(column=2, row=0)

label1 = tk.Label(text="is equal to")
label1.grid(column=0, row=1)


label2 = tk.Label(text="0")
label2.grid(column=1, row=1)

label3 = tk.Label(text="Km")
label3.grid(column=2, row=1)

# ---------------- #

def calculate():
    try:
        n = int(input.get())
        label2.config(text=round(n * 1.609, 2))
    except ValueError:
        label2.config(text="0")
    except TypeError:
        label2.config(text="0")
    
                                                                                                                                                                               

button = tk.Button(text="Calculate", command=calculate)
button.grid(column=1, row=2)

input = tk.Entry()
input.config(width=10)
input.grid(column=1, row=0)

window.mainloop()
