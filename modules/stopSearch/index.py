from tkinter import *
from utils.widgets import optionMenu
from utils.widgets import tkLabel
from modules.stopSearch.stopSearchFunc import ageRange, searchPurpose, ethnicity
# , plotViewRangeCases
from utils.filterParams import monthList, yearList, dayList
from utils.requests import fetchPoliceForce

def ageGenderEthnicity(form):    
    if len(form.winfo_children()) > 0:
        for widget in form.winfo_children():
            widget.destroy()

    month = StringVar(form)
    month.set(monthList()[0])
    tkLabel(form, text="Month", x=190, y=10)
    optionMenu(form, month, monthList(), x=190, y=36)

    ###############################################################
    
    year = StringVar(form)
    year.set(yearList()[0])
    tkLabel(form, text="Year", x=190, y=71)
    optionMenu(form, year, yearList(), x=190, y=96)
    
    ###############################################################
    options = list(fetchPoliceForce().keys())
    policeForce = StringVar(form)
    policeForce.set(options[1])
    tkLabel(form, text="Police Force: ", x=190, y=130)
    optionMenu(form, policeForce, options, x=190, y=155)
    
    func = lambda: ageRange(
        month.get(),
        year.get(),
        policeForce.get(),
    )
    
    func1 = lambda: searchPurpose(
        month.get(),
        year.get(),
        policeForce.get(),
    )
    
    func2 = lambda: ethnicity(
        month.get(),
        year.get(),
        policeForce.get(),
    )

    Button(form, text="View By Age Range", command=func).place(x=190, y=195)
    Button(form, text="View By Search Purpose", command=func1).place(x=190, y=230)
    Button(form, text="View By Ethnicity",command=func2).place(x=190, y=270)
    
    
# def viewRangeCases(form):    
#     if len(form.winfo_children()) > 0:
#         for widget in form.winfo_children():
#             widget.destroy()

#     startMonth = StringVar(form)
#     startMonth.set(monthList()[0]) # default value of dropdown

#     tkLabel(form, text="From (Start Month)", x=25, y=10)
#     optionMenu(form, startMonth, monthList(), x=33, y=34)

#     endMonth = StringVar(form)
#     endMonth.set(monthList()[1]) 
#     tkLabel(form, text="To (End Month)", x=350, y=10)
#     optionMenu(form, endMonth, monthList(), x=358, y=34)

#     ##############################################################
#     yearList = [2020, 2021, 2022]
#     startYear = StringVar(form)
#     startYear.set(yearList[0])
#     tkLabel(form, text="From (Start Year)", x=25, y=74)
#     optionMenu(form, startYear, yearList, x=33, y=100)

#     endYear = StringVar(form)
#     endYear.set(yearList[1])
#     tkLabel(form, text="To (End Year)", x=350, y=74)
#     optionMenu(form, endYear, yearList, x=350, y=100)

#     ###############################################################
#     options = list(fetchPoliceForce().keys())
#     policeForce = StringVar(form)
#     policeForce.set(options[0])
#     tkLabel(form, text="Police Force", x=25, y=135)
#     optionMenu(form, policeForce, options, x=33, y=162)
    
#     ###############################################################

#     func = lambda: plotViewRangeCases(
#         startMonth.get(),
#         endMonth.get(),
#         startYear.get(),
#         endYear.get(),
#         policeForce.get(),
#     )

#     Button(form, text="View", command=func).place(x=210, y=210)
 