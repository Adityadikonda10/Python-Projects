from tkinter import *
import pandas as p
from random import choice

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}
# --------------------------------- READING FILE --------------------------------- #
try:
     data = p.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
     orignal_data = p.read_csv("data/korean_words.csv")
     to_learn = orignal_data.to_dict(orient="records")
else:
     to_learn = data.to_dict(orient="records")


# --------------------------------- GET WORD --------------------------------- #
def new_card():
     global current_card, flip_timer
     window.after_cancel((flip_timer))
     current_card = choice(to_learn)
     canvas.itemconfig(card_img, image=FRONT_IMG)
     canvas.itemconfig(card_title, text="Korean", fill="black")
     canvas.itemconfig(card_word, text=current_card['Korean'], fill="black")
     flip_timer=window.after(3000, func=flip_card)

# -------------------------------------------- FLIP CARD -------------------------------------------- #
def flip_card():
     # global current_card
     canvas.itemconfig(card_img, image=BACK_IMG)
     canvas.itemconfig(card_title, text="English", fill="white")
     canvas.itemconfig(card_word, text=current_card['English'], fill="white")

# --------------------------------- RIGHT --------------------------------- #
def right():
     to_learn.remove(current_card)
     data = p.DataFrame(to_learn)
     data.to_csv("./data/words_to_learn.csv", index=False)
     new_card()


# --------------------------------- ERONG --------------------------------- #
def wrong():
     new_card()

# -------------------------------------------- UI SETUP -------------------------------------------- #
window = Tk()
window.title("Korean Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)


# --------------------------------- CANVAS --------------------------------- #
FRONT_IMG = PhotoImage(file="./images/card_front.png")
BACK_IMG = PhotoImage(file="./images/card_back.png")

flip_timer = window.after(20000, func=flip_card)

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_img = canvas.create_image(400, 263, image=FRONT_IMG)
card_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"), fill="black")
card_word = canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"), fill="black")
canvas.grid(row=0, column=0, columnspan=2)

# --------------------------------- WRONG BUTTON --------------------------------- #
wrong_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=wrong)
wrong_button.config(borderwidth=0, border=0)
wrong_button.grid(row=1, column=0)

# --------------------------------- RIGHT BUTTON --------------------------------- #
right_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=right)
right_button.config(borderwidth=0, border=0)
right_button.grid(row=1, column=1)










new_card()
window.mainloop()