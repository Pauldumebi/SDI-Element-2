from tkinter import *
from utils.widgets import optionMenu
from utils.widgets import tkLabel
from modules.covid.covidFunc import plotDailyCases, viewTopFiveRegionWithHighestCases, plotTwoRegions, plotByMonths
from utils.filterParams import regionList, monthList, yearList, dayList

def destroyFrame(form):
    # clear the window so you can render new widgets
    if len(form.winfo_children()) > 0:
        for widget in form.winfo_children():
            widget.destroy()
            
def dailyAndCumulativeCases(form):
    destroyFrame(form)
    
    startDay = StringVar(form)
    startDay.set(dayList()[0]) # default value of dropdown

    tkLabel(form, text="From (Start Day)", x=25, y=10)
    optionMenu(form, startDay, dayList(), x=33, y=34)

    endDay = StringVar(form)
    endDay.set(dayList()[1]) 
    tkLabel(form, text="To (End Day)", x=350, y=10)
    optionMenu(form, endDay, dayList(), x=358, y=34)

    ##############################################################

    startMonth = StringVar(form)
    startMonth.set(monthList()[0])
    tkLabel(form, text="From (Start Month)", x=25, y=74)
    optionMenu(form, startMonth, monthList(), x=33, y=100)

    endMonth = StringVar(form)
    endMonth.set(monthList()[1])
    tkLabel(form, text="To (End Month)", x=350, y=74)
    optionMenu(form, endMonth, monthList(), x=350, y=100)

    ###############################################################

    startYear = StringVar(form)
    startYear.set(yearList()[0])
    tkLabel(form, text="From (Start Year)", x=25, y=140)
    optionMenu(form, startYear, yearList(), x=33, y=165)

    endYear = StringVar(form)
    endYear.set(yearList()[0])
    tkLabel(form, text="To (End Year)", x=350, y=140)
    optionMenu(form, startYear, yearList(), x=350, y=165)

    ###############################################################

    region = StringVar(form)
    region.set(regionList()[0])
    tkLabel(form, text="Select region: ", x=50, y=210)
    optionMenu(form, region, regionList(), x=150, y=210)
    
    func = lambda: plotDailyCases(
        "Daily infection rate",
        startDay.get(),
        endDay.get(),
        startMonth.get(),
        endMonth.get(),
        startYear.get(),
        endYear.get(),
        region.get(),
    )
    
    func1 = lambda: plotDailyCases(
        "%Change in Daily infection rate",
        startDay.get(),
        endDay.get(),
        startMonth.get(),
        endMonth.get(),
        startYear.get(),
        endYear.get(),
        region.get(),
    )

    Button(form, text="Daily Infection rate plot", command=func).place(x=160, y=250)
    Button(form, text="%Change in daily Infection rate plot", command=func1).place(x=140, y=290)
    
    
def topFiveRegionWithHighestCases(form):  
    destroyFrame(form) 
           
    startDay = StringVar(form)
    startDay.set(dayList()[0]) # default value of dropdown

    tkLabel(form, text="From (Start Day)", x=25, y=10)
    optionMenu(form, startDay, dayList(), x=33, y=34)

    endDay = StringVar(form)
    endDay.set(dayList()[1]) 
    tkLabel(form, text="To (End Day)", x=350, y=10)
    optionMenu(form, endDay, dayList(), x=358, y=34)

    ##############################################################

    startMonth = StringVar(form)
    startMonth.set(monthList()[0])
    tkLabel(form, text="From (Start Month)", x=25, y=74)
    optionMenu(form, startMonth, monthList(), x=33, y=100)

    endMonth = StringVar(form)
    endMonth.set(monthList()[1])
    tkLabel(form, text="To (End Month)", x=350, y=74)
    optionMenu(form, endMonth, monthList(), x=350, y=100)

    ###############################################################

    startYear = StringVar(form)
    startYear.set(yearList()[0])
    tkLabel(form, text="From (Start Year)", x=25, y=140)
    optionMenu(form, startYear, yearList(), x=33, y=165)

    endYear = StringVar(form)
    endYear.set(yearList()[0])
    tkLabel(form, text="To (End Year)", x=350, y=140)
    optionMenu(form, startYear, yearList(), x=350, y=165)
    
    func = lambda: viewTopFiveRegionWithHighestCases(
        startDay.get(),
        endDay.get(),
        startMonth.get(),
        endMonth.get(),
        startYear.get(),
        endYear.get(),
    )

    Button(form, text="View", command=func).place(x=200, y=210)
    
def compareTwoRegions(form):    
    destroyFrame(form)
    
    startDay = StringVar(form)
    startDay.set(dayList()[0]) # default value of dropdown

    tkLabel(form, text="From (Start Day)", x=25, y=10)
    optionMenu(form, startDay, dayList(), x=33, y=34)

    endDay = StringVar(form)
    endDay.set(dayList()[1]) 
    tkLabel(form, text="To (End Day)", x=350, y=10)
    optionMenu(form, endDay, dayList(), x=358, y=34)

    ##############################################################

    startMonth = StringVar(form)
    startMonth.set(monthList()[2])
    tkLabel(form, text="From (Start Month)", x=25, y=74)
    optionMenu(form, startMonth, monthList(), x=33, y=100)

    endMonth = StringVar(form)
    endMonth.set(monthList()[3])
    tkLabel(form, text="To (End Month)", x=350, y=74)
    optionMenu(form, endMonth, monthList(), x=350, y=100)

    ###############################################################

    startYear = StringVar(form)
    startYear.set(yearList()[0])
    tkLabel(form, text="From (Start Year)", x=25, y=140)
    optionMenu(form, startYear, yearList(), x=33, y=165)

    endYear = StringVar(form)
    endYear.set(yearList()[0])
    tkLabel(form, text="To (End Year)", x=350, y=140)
    optionMenu(form, startYear, yearList(), x=350, y=165)
    
    ###############################################################

    startRegion = StringVar(form)
    startRegion.set(regionList()[0])
    tkLabel(form, text="First region: ", x=25, y=210)
    optionMenu(form, startRegion, regionList(), x=32, y=235)
    
    endRegion = StringVar(form)
    endRegion.set(regionList()[1])
    tkLabel(form, text="Second region: ", x=350, y=210)
    optionMenu(form, endRegion, regionList(), x=350, y=235)
    
    func = lambda: plotTwoRegions(
        startDay.get(),
        endDay.get(),
        startMonth.get(),
        endMonth.get(),
        startYear.get(),
        endYear.get(),
        startRegion.get(),
        endRegion.get(),
    )

    Button(form, text="View", command=func).place(x=200, y=280)
    
def viewByMonths(form):    
    destroyFrame(form)

    month = StringVar(form)
    month.set(monthList()[0])
    tkLabel(form, text="Month", x=210, y=24)
    optionMenu(form, month, monthList(), x=210, y=50)

    ###############################################################

    year = StringVar(form)
    year.set(yearList()[0])
    tkLabel(form, text="Year", x=210, y=85)
    optionMenu(form, year, yearList(), x=210, y=110)
    
    ###############################################################
    
    func = lambda: plotByMonths(
        month.get(),
        year.get(),
    )

    Button(form, text="View", command=func).place(x=210, y=155)
    