from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
TIME = 3
current_card = {}

def word_known():
    to_learn.remove(current_card)
    next_card()
    data=pandas.DataFrame(to_learn)
    data.to_csv("data/updated_words.csv", index= False)
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    french_word = current_card["French"]
    canvas.itemconfig(title, text="French", fill="black")
    canvas.itemconfig(word, text=f"{french_word}", fill="black")
    canvas.itemconfig(card_face, image=card_front)
    flip_timer=window.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(card_face, image=card_back)
    canvas.itemconfig(title, fill="white", text="English")
    canvas.itemconfig(word, fill="white", text=current_card["English"])


# ----------------------------UI setup----------------------------#

window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, padx=10, pady=10)
flip_timer=window.after(3000, flip_card)

try:
    data = pandas.read_csv("./data/updated_words.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("./data/french_words.csv")
    to_learn= original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

card_back = PhotoImage(file="./images/card_back.png")
card_front = PhotoImage(file="./images/card_front.png")
card_face = canvas.create_image(400, 263, image=card_front)
title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))

tick_image = PhotoImage(file="./images/right.png")
right_button = Button(image=tick_image, width=100, highlightthickness=0, relief="groove", command=word_known)
right_button.grid(row=1, column=0)

cross_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=cross_image, width=100, highlightthickness=0, relief="groove", command=next_card)
wrong_button.grid(row=1, column=1)

next_card()

window.mainloop()
