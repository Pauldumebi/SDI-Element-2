from tkinter import ttk
from utils.widgets import tkLabel
import tkinter as tk
from modules.covid.index import dailyAndCumulativeCases, topFiveRegionWithHighestCases, compareTwoRegions, viewByMonths
root = tk.Tk()
root.geometry("750x550")
root.title("Software for digital innovation element 2")

tabControl = ttk.Notebook(root)
covidTab = tk.Frame(tabControl)
stopSearchTab = tk.Frame(tabControl)

tabControl.add(covidTab, text="Covid Report")
tabControl.add(stopSearchTab, text="Stop and Search")
tabControl.pack(expand=1, fill="both")

tkLabel(covidTab, text="This tab shows the visualization for covid report...🤦🏻‍♂️ to be continued", x=0, y=5)
tkLabel(stopSearchTab, text="This tab shows the visualization for Stop and Search...(to be continued 😂)", x=0, y=5)

tk.Button(covidTab, text= "Daily and %Change in daily Cases", command=lambda: dailyAndCumulativeCases(form)).place(x=100, y=40)
tk.Button(covidTab, text= "Compare two Regions", command=lambda: compareTwoRegions(form)).place(x=340, y=40) 
tk.Button(covidTab, text= "Top regions with the highest cases", command=lambda: topFiveRegionWithHighestCases(form)).place(x=100, y=70)
tk.Button(covidTab, text= "View cases by Months", command=lambda: viewByMonths(form)).place(x=350, y=70)  
 
form = tk.Frame(root, width=500, height=330)
form.place(x=100, y=140)

root.mainloop()