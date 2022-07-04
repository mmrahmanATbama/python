# this is just some random stuff.

import tkinter

window = tkinter.Tk()
window.title("Test Window")
window.minsize(width=500, height=300)

# Label
my_label = tkinter.Label(text="I am a Label", font=("Arial", 18))
my_label.pack()


# Button
def button_clicked():
    new_text = input.get()
    my_label.config(text=new_text)

button = tkinter.Button(text="Click me", command=button_clicked)
button.pack()

# Entry
input = tkinter.Entry(width=10)
input.pack()


# Advanced Python Arguments
# veriadic function: unlimited number of arguments

def add(*args):
    num = 0
    for number in args:
        num = num + number
    return num


print(add(1, 2, 3, 4, 5))


# **kwargs: May keyworded arguments

def calculate(n, **kwargs):
    for key, value in kwargs.items():
        print(kwargs)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)


class Car:
    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")


my_car = Car(make="Hyuandai")
print(my_car.make)

window.mainloop()
