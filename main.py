from tkinter import ttk
from utils.widgets import tkLabel
import tkinter as tk
from modules.covid.index import dailyAndCumulativeCases, topFiveRegionWithHighestCases, compareTwoRegions, viewByMonths
from modules.stopSearch.index import ageGenderEthnicity

def tkinter_app():

    root = tk.Tk()
    root.geometry("750x600")
    # root.geometry("+%d+%d" % (250, 10))
    root.title("Software for digital innovation element 2")

    tabControl = ttk.Notebook(root)
    covidTab = tk.Frame(tabControl)
    stopSearchTab = tk.Frame(tabControl)

    tabControl.add(covidTab, text="Covid Report")
    tabControl.add(stopSearchTab, text="Stop and Search")
    tabControl.pack(expand=1, fill="both")

    tkLabel(covidTab, text="This tab shows the different type of visualization used for this project for covid report. Click any of the buttons below to get started", x=0, y=5)
    tkLabel(stopSearchTab, text="This tab shows the visualization used for Stop and Search api provided by the UK police)", x=0, y=5)
 
    tk.Button(covidTab, text= "Daily and %Change in daily Cases", command=lambda: dailyAndCumulativeCases(form)).place(x=100, y=40)
    tk.Button(covidTab, text= "Compare two Regions", command=lambda: compareTwoRegions(form)).place(x=340, y=40) 
    tk.Button(covidTab, text= "Top regions with the highest cases", command=lambda: topFiveRegionWithHighestCases(form)).place(x=100, y=70)
    tk.Button(covidTab, text= "View cases by Months", command=lambda: viewByMonths(form)).place(x=350, y=70)  
    
    form = tk.Frame(covidTab, width=500, height=400)
    form.place(x=100, y=120)

    form2 = tk.Frame(stopSearchTab, width=500, height=400)
    form2.place(x=100, y=50)

    ageGenderEthnicity(form2)
    
    return root

if __name__ == "__main__":
    tkinter_app().mainloop()