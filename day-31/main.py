import tkinter as tk
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/german_words.csv")
    to_learn = original_data.to_dict(orient="records")
except pandas.errors.EmptyDataError:
    original_data = pandas.read_csv("data/german_words.csv")
    to_learn = original_data.to_dict(orient="records")
    original_data.to_csv("data/words_to_learn.csv", index=False)
else:
    to_learn = data.to_dict(orient="records")


# ---------- FN SETUP ---------- #

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    
    current_card = random.choice(to_learn)
    
    canvas.itemconfig(card_title, text="German", fill="black")
    canvas.itemconfig(card_text, text=current_card["German"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    
    flip_timer = window.after(3000, func=flip_card)
    
def is_known():
    global to_learn
    to_learn.remove(current_card)
    
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    
    try:
        next_card()
    except IndexError:
        original_data = pandas.read_csv("data/german_words.csv")
        to_learn = original_data.to_dict(orient="records")
        original_data.to_csv("data/words_to_learn.csv", index=False)
        next_card()
    
def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_text, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)


# ---------- UI SETUP ---------- #
window = tk.Tk()
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.minsize(900, 700)
window.maxsize(900, 700)
window.title("Flashy")

flip_timer = window.after(3000, func=flip_card)

canvas = tk.Canvas(width=800, height=526)
card_front_img = tk.PhotoImage(file="images/card_front.png")
card_back_img = tk.PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)

card_title = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
card_text = canvas.create_text(400, 260, text="", font=("Arial", 60, "bold"))

canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

unknown_button_img = tk.PhotoImage(file="images/wrong.png")
unknown_button = tk.Button(image=unknown_button_img, cursor="hand2", command=next_card)
unknown_button.grid(row=1, column=0)

known_button_img = tk.PhotoImage(file="images/right.png")
known_button = tk.Button(image=known_button_img, cursor="hand2", command=is_known)
known_button.grid(row=1, column=1)

next_card()

window.mainloop()