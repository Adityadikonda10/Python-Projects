from tkinter import *

THEME_COLOR = "#375362"


class UserInterface:
    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.canvas.config(borderwidth=0)
        self.canvas.grid(column=0, row=1, columnspan=2)
        # self.question = self.canvas.create_text(0, 0, text=f"Question", font=("Arial", 20, "italic"), fill=THEME_COLOR)

        self.true_photo = PhotoImage("/images/true.png")
        self.true_button = Button(image=self.true_photo, highlightthickness=0, borderwidth=0, border=THEME_COLOR)
        self.true_button.grid(column=0, row=2)

        self.false_photo = PhotoImage("/images/false.png")
        self.false_photo = Button(image=self.false_photo, highlightthickness=0, borderwidth=0, border=THEME_COLOR)
        self.false_photo.grid(column=1, row=2)

        self.window.mainloop()
