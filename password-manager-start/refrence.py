from tkinter import *
import math
# from numpy.distutils.system_info import p

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
mark = []
timer = None
# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    timer_label.config(text = "Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text = "00:00")
    mark.clear()
    checkmark.config(text="".join(mark))
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN* 60
    lonk_break_sec = LONG_BREAK_MIN*60

    if reps % 8 == 0:
        count_down(lonk_break_sec)
        timer_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        timer_label.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec =f"0{count_sec}"
    # elif count_min < 10:
    #     count_min = f"0{count_min}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        if reps % 2 == 0:
            mark.append("✔")
            checkmark.config(text="".join(mark))

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


# ------------------------------------------------------------canvas---------------------------------------------------------------- #
canvas = Canvas(width=200 ,height=224, bg=YELLOW, highlightthickness=0)
photo = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=photo)
timer_text = canvas.create_text(100, 130, text="00:00",fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# ------------------------------------------------------------Label---------------------------------------------------------------- #
timer_label = Label(text="Timer", font=(FONT_NAME, 50, "bold"), bg=YELLOW, highlightthickness=0)
timer_label.config(padx=5,pady=5, fg=GREEN)
timer_label.grid(column=1, row=0)

# ------------------------------------------------------------start button---------------------------------------------------------------- #
start_button = Button(text="Start", bg=YELLOW, command=start_timer, highlightthickness=0)
start_button.config(padx=5, pady=5, borderwidth=0, border=0)
start_button.grid(column=0, row=2)

# ------------------------------------------------------------start button---------------------------------------------------------------- #
reset_button = Button(text="Reset", bg=YELLOW, command=reset_timer , highlightthickness=0)
reset_button.config(padx=5, pady=5, borderwidth=0, border=0)
reset_button.grid(column=2, row=2)

# ------------------------------------------------------------start button---------------------------------------------------------------- #
checkmark = Label(bg=YELLOW, font=("",22,""), highlightthickness=0)
checkmark.grid(column=1, row=3)
checkmark.config(padx=5, pady=5, fg=GREEN)

# ------------------------------------------------------------Empty label---------------------------------------------------------------- #
empty_lebel1 = Label(text=" ", font=(FONT_NAME, 20, "bold"), bg=YELLOW, highlightthickness=0)
empty_lebel1.config(padx=5,pady=5)
empty_lebel1.grid(column=0, row=4)

empty_lebel2 = Label(text=" ", font=(FONT_NAME, 20, "bold"), bg=YELLOW, highlightthickness=0)
empty_lebel2.config(padx=5,pady=5)
empty_lebel2.grid(column=0, row=4)










window.mainloop()
