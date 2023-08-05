from tkinter import *



def calculate():
    miles = int(input.get())
    km = miles * 1.6
    my_label3.config(text=int(km))





window = Tk()
window.title("Miles To Km Converter")
window.minsize(width=60, height=100)
window.config(padx=10, pady=10)

#Entry
input = Entry(width=10)
print(input.get())
input.grid(column=1, row=0)

#Label1
my_label1 = Label(text="Miles ", font=("Arial", 12, "bold"))
my_label1.grid(column=2, row=0)
my_label1.config(padx=5, pady=5)

#Label2
my_label2 = Label(text="is equal to ", font=("Arial", 12, "bold"))
my_label2.grid(column=0, row=1)
my_label2.config(padx=5, pady=5)


#Label4
my_label4 = Label(text="km ", font=("Arial", 12, "bold"))
my_label4.grid(column=2, row=1)
my_label4.config(padx=5, pady=5)

#Button
button = Button(text="Calculate", command=calculate)
button.grid(column=1, row=2)
# print(c.result())
#Label3
my_label3 = Label(text=f"{0} ", font=("Arial", 12, "bold"))
my_label3.grid(column=1, row=1)
my_label3.config(padx=5, pady=5)





window.mainloop()