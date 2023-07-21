from tkinter import *


def calculate():
    miles = float(input_miles.get())
    kms = miles * 1.6
    kms_value.config(text=f"{kms} Kms")


window = Tk()
window.title("Miles To Kilometers Converter")
window.minsize(width=200, height=200)
window.config(padx=50,pady=50)

input_miles = Entry(width=10)
input_miles.grid(row=0, column=1)

miles = Label(text="Miles")
miles.grid(row=0, column=2)

text = Label(text="is equal to")
text.grid(row=1, column=0)

kms_value = Label(text="0 Kms")
kms_value.grid(row=1, column=1)

button = Button(text="Calculate", command=calculate)
button.grid(row=2, column=1)

mainloop()
