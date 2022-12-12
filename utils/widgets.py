from tkinter import *

def tkLabel (window, text, x, y):
    label = Label(window, text=text, font=("Arial", 12))
    label.place( x=x, y=y)
    
    return label

def optionMenu(window, val, OPTIONS, x, y):
    
    dropDownMenu = OptionMenu(window, val, *OPTIONS)
    dropDownMenu.place(x=x, y=y)
    
    return dropDownMenu
