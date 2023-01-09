from modules.stopSearch.requests import fetchCasesRequest
from utils.monthList import monthsDict
from tkinter import messagebox
import pandas as pd
from charts.index import pieChart, lollipopChart, dotPlot, donutChart, verticalBarChart
import timeit

def validateDate(year, month):
    try:
        date = year + "-" + monthsDict()[month]
    except:
        messagebox.showinfo(
            "showinfo", "Invalid Date was selected, select from dropdown only"
        )
    return date

def isRequestEmpty(month, year, policeForce):
    date = validateDate(year, month)
    data = fetchCasesRequest(policeForce, date)[1]  #list contains two items length which is first and data
    if len(data) <= 1: #Checks to see the response isn't empty
        return messagebox.showinfo("showinfo", "No Data for the selected month")
    else: 
        return data  
        
def ageRange(month, year, policeForce):
    # start = timeit.default_timer() 

    df = pd.DataFrame.from_dict(isRequestEmpty(month, year, policeForce))
    data = df.groupby(['age_range'], as_index=False).count()
    if len(data) <= 1:
        return messagebox.showinfo("showinfo", "No Data for the selected month for " + policeForce)
    title = "Stop and Search Cases Breakdown by Age Range for " + policeForce + " in " + month + ", " + year
    pieChart(title, data["involved_person"], data["age_range"])
    
    # stop = timeit.default_timer()
    # print('Time - ageRange: ', stop - start)  
    return data, title
    
ylabel="Number of Persons Involved"

def searchPurpose(month, year, policeForce):
    
    df = pd.DataFrame.from_dict(isRequestEmpty(month, year, policeForce))
    data = df.groupby(["object_of_search"], as_index=False)[["involved_person"]].count()
    if len(data) <= 1:
        return messagebox.showinfo("showinfo", "No Data for the selected month for " + policeForce)
    maxValue=data.max()
    max = maxValue['involved_person'] #gets the max value in the dataFrame
    title = "Stop and Search Cases Breakdown by Search Purpose for " + policeForce + " in " + month + ", " + year
    print(type(max), 'maxValue')
    dotPlot(data.index, data["involved_person"], data["object_of_search"], max, ylabel, title=title)
    return data, max, ylabel, title
    
    
def ethnicity(month, year, policeForce):
    start = timeit.default_timer() 
    
    df = pd.DataFrame.from_dict(isRequestEmpty(month, year, policeForce))
    data = df.groupby(["officer_defined_ethnicity"], as_index=False)[["involved_person"]].count()
    if len(data) <= 1:
        return messagebox.showinfo("showinfo", "No Data for the selected month for " + policeForce)
    maxValue=data.max()
    max = maxValue['involved_person'] #gets the max value in the dataFrame
    title = "Stop and Search Cases Breakdown by Ethnicity for " + policeForce + " in " + month + ", " + year

    lollipopChart(data.index, data["involved_person"], data["officer_defined_ethnicity"], max, ylabel, title=title, data=data)
    return data, max, ylabel, title
    
def outcome(month, year, policeForce):
    
    df = pd.DataFrame.from_dict(isRequestEmpty(month, year, policeForce))
    data = df.groupby(["outcome"], as_index=False)[["involved_person"]].count()
    if len(data) <= 1:
        return messagebox.showinfo("showinfo", "No Data for the selected month for " + policeForce)
    title = "Stop and Search Cases Outcome for " + policeForce + " in " + month + ", " + year
    verticalBarChart(title, data, data["involved_person"], data["outcome"] )
    return data, title
    
def gender(month, year, policeForce):
    
    df = pd.DataFrame.from_dict(isRequestEmpty(month, year, policeForce))
    data = df.groupby(["gender"], as_index=False)[["involved_person"]].count()
    if len(data) <= 1:
        return messagebox.showinfo("showinfo", "No Data for the selected month for " + policeForce)
    title = "Stop and Search Cases Breakdown by Gender for " + policeForce + " in " + month + ", " + year
    explode = (0.05, 0.05)
    donutChart(title, data["involved_person"], data["gender"], explode)
    return data, title, explode