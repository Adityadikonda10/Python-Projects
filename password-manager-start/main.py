from tkinter import *
from tkinter import messagebox
from random import randint, shuffle, choice
import pandas as p
import pyperclip as pc
import json

from six import b
FONT_NAME = "Proxima Nova"
LIGHTER = "#DDE6ED"
LIGHT = "#9DB2BF"
LIGHT2="#9DB2BF"
MEDIUM = "#526D82"
DARK = "#27374D"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_entry.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for char in range(randint(8, 10))]
    password_symbols = [choice(symbols) for s in range(randint(2, 4))]
    password_numbers = [choice(numbers) for n in range(randint(2, 4))]
    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    pc.copy(password)

    password_entry.insert(END, string=f"{password}")
    # print(f"Your password is: {password}")


    # ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website_name = website_entry.get()
    email_username_name = email_username_entry.get()
    password = password_entry.get()
    new_data = {
        website_name: {
            "email_username": email_username_name,
            "password": password
        }
    }
    if len(website_name) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Don't leave any field empty")

    else:
        try:
            with open("passwords.json", "r") as f:
                data = json.load(f)
                data.update(new_data)
            with open("passwords.json", "w") as f:
                json.dump(data, f, indent=4)
                website_entry.delete(0, END)
                password_entry.delete(0, END)
        except FileNotFoundError:
            with open("passwords.json", "w") as f:
                json.dump(new_data, f, indent=4)
                website_entry.delete(0, END)
                password_entry.delete(0, END)

    # ---------------------------- SEARCH ------------------------------- #
def search():
    website = website_entry.get()
    with open("passwords.json", 'r') as f:
        data = json.load(f)
        if website in data:
            email = data[website]['email_username']
            password = data[website]['password']
            messagebox.showinfo(title=website_entry.get(), message=f"E-mail/Username: {email} \n Password: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("My Password Generator")
window.config(padx=50, pady=50, bg=LIGHTER)

# ---------------------------- Canvas ------------------------------- #
canvas = Canvas(width=200, height=200, bg=LIGHTER, highlightthickness=0)
photo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=photo)
canvas.grid(row=0, column=1)

# ---------------------------- website label ------------------------------- #
website_label = Label(text="Website:", font=(FONT_NAME, 15, "normal"), bg=LIGHTER, highlightthickness=0)
website_label.config(padx=5, pady=5, fg=MEDIUM)
website_label.grid(row=1, column=0)

# ---------------------------- email/username label ------------------------------- #
email_username_label = Label(text="E-mail/Username:", font=(FONT_NAME, 15, "normal"), bg=LIGHTER, highlightthickness=0)
email_username_label.config(padx=5, pady=5, fg=MEDIUM)
email_username_label.grid(row=2, column=0)

# ---------------------------- website label ------------------------------- #
password_label = Label(text="Password:", font=(FONT_NAME, 15, "normal"), bg=LIGHTER, highlightthickness=0)
password_label.config(padx=5, pady=5, fg=MEDIUM)
password_label.grid(row=3, column=0)


# ---------------------------- website entry -------------------------------- #
website_entry = Entry(width=21,bg=LIGHT2, highlightthickness=0.2)
# website_entry.insert(END, string="Enter website name")
website_entry.focus()
website_entry.config(highlightbackground=LIGHT2, highlightcolor=LIGHT2, border=0.5, fg=DARK)
website_entry.grid(row=1, column=1)

# ---------------------------- search button -------------------------------- #
search_button = Button(width=10, text="Search", bg=MEDIUM, highlightthickness=0, command=search)
search_button.config(padx=2, pady=2, border=0, borderwidth=0, fg=DARK)
search_button.grid(column=2, row=1)

# ---------------------------- E-mail/Username entry -------------------------------- #
email_username_entry = Entry(width=35,bg=LIGHT2, highlightthickness=0.2)
email_username_entry.insert(0, "indianamigo717@gmail.com")
email_username_entry.config(highlightbackground=LIGHT2, highlightcolor=LIGHT2, border=0.5, fg=DARK)
email_username_entry.grid(row=2, column=1, columnspan=2)

# ---------------------------- Password entry -------------------------------- #
password_entry = Entry(width=21 ,bg=LIGHT2, highlightthickness=0.2)
# password_entry.insert(END, string="Enter a Password")
password_entry.config(highlightbackground=LIGHT, highlightcolor=LIGHT, border=0.5, fg=DARK)
password_entry.grid(row=3, column=1)


# ---------------------------- generate password button -------------------------------- #
generate_password_button = Button(width=10, text="Generate Password", bg=MEDIUM, highlightthickness=0, command=generate_password)
generate_password_button.config(padx=2, pady=2, border=0, borderwidth=0, fg=DARK)
generate_password_button.grid(column=2, row=3)


# ---------------------------- add button -------------------------------- #
add_button = Button( width=32 ,text="Add", bg=MEDIUM, highlightthickness=0, command=save)
add_button.config(padx=2, pady=2, border=0, borderwidth=0, fg=DARK)
add_button.grid(column=1, row=4, columnspan=2)
















window.mainloop()


