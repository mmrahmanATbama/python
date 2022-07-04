"""
Unit converter.
Initially just the mile to kilometer converter.
Improvements:
1. Offer other unit conversions a typical US resident may find helpful.
2. See how this can be incorporated in a website in the future. (less work to develop the page, just plug this in
if possible)

from tkinter import *
"""
import tkinter

# create a new window
from tkinter import END

window = tkinter.Tk()
window.title("Unit Converter")
window.config(padx=40, pady=40)
#window.minsize(width=500, height=300)


# for miles to kilometer, need one entry, four labels and one button
# use grid
# create four labels:

def calculate_button_clicked():
    miles = float(entry.get())
    kilometer = "{:.2f}". format(miles * 1.609)

    # kilometer is going to be a string, so wrap it around f string
    converted_label.config(text=f"{kilometer}")


unit_label = tkinter.Label(text="Miles", font=("Arial", 12))
unit_label.grid(column=2, row=0)

equal_to_label = tkinter.Label(text="is equal to ", font=("Arial", 12))
equal_to_label.grid(column=0, row=1)

converted_label = tkinter.Label(text="0.0")
converted_label.grid(column=1, row=1)

converted_unit = tkinter.Label(text="Km", font=("Arial", 12))
converted_unit.grid(column=2, row=1)

entry = tkinter.Entry(width=5)
entry.insert(END, 0)
entry.grid(column=1, row=0)

button = tkinter.Button(text="Calculate", font=("Arial", 12), command=calculate_button_clicked)
button.grid(column=1, row=2)

window.mainloop()
