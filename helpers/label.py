import tkinter as tkt

def label(window, text, x, y):
    label = tkt.Label(window, text=text, font=("Arial", 11))
    label.place(x=x, y=y)

    return label