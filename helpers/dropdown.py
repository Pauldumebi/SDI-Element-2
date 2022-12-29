import tkinter as tkt

def dropdown(window, val, options, x, y):

    dropDownMenu = tkt.OptionMenu(window, val, *options)
    dropDownMenu.place(x=x, y=y)

    return dropDownMenu