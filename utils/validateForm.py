from tkinter import messagebox
import datetime as dt
from utils.filterParams import monthList, yearList, dayList
from utils.monthsDict import monthsDict

def validateForm(
    startDay,
    endDay,
    startMonth,
    endMonth,
    startYear,
    endYear,
    firstRegion="",
    secondRegion="",
):
    
    try:
        startDate = dt.datetime(
            day=int(startDay),
            month=int(monthsDict()[startMonth]),
            year=int(startYear),
        )
        endDate = dt.datetime(
            day=int(endDay), month=int(monthsDict()[endMonth]), year=int(endYear)
        )
        maxDate = dt.datetime(day=int(dayList()[0]), month=int(monthsDict()[monthList()[-1]]), year=int(yearList()[0]))     
    except:
        messagebox.showinfo("showinfo", "Invalid Date, select again")
    
    if len(firstRegion) and len(secondRegion):
        if firstRegion == secondRegion:
            return messagebox.showinfo("showinfo", "Invalid selection cannot compare same region")
    
    if startDate > endDate:
       return messagebox.showinfo("showinfo", "Invalid Date selected(start date cannot be greater than end date!!)")

    elif (startDate > maxDate) or (endDate > maxDate):
        return messagebox.showinfo("showinfo", "Invalid Date selected")
    
    else:
        return startDate, endDate
    
  