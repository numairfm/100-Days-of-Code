import tkinter as tk

def button_clicked():
    print("OW")
    my_label.config(text=input.get())

window = tk.Tk()
window.title("First GUI Program")
window.minsize(width=500, height=300)

my_label = tk.Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.grid(column=0, row=0)

my_label.config(text="New Text")


button = tk.Button(text="touch me", command=button_clicked)
button.grid(column=1, row=1)

button2 = tk.Button(text="touch me", command=button_clicked)
button2.grid(column=2, row=0)

input = tk.Entry(width=10)
input.grid(column=3, row=3)



window.mainloop()


