from utils.requests import fetchCasesRequest
from utils.monthsDict import monthsDict
from tkinter import messagebox
import pandas as pd
from charts.index import pieChart, lollipopChart, dotPlot
# , horizontalBarChart, barChart
# import datetime as dt
from utils.validateForm import validateForm

def validateDate(year, month):
    try:
        date = year + "-" + monthsDict()[month]
    except:
        # if test == False:
            messagebox.showinfo(
                "showinfo", "Invalid Date was selected, select from dropdown only"
            )
        # else:
        #     return "error"
    return date

def isRequestEmpty(month, year, policeForce):
    date = validateDate(year, month)
    data = fetchCasesRequest(policeForce, date)[1]  #list contains two items length which is first and data
    if data == []:
        # if test == False:
            messagebox.showinfo("showinfo", "No Data for the selected month")
        # else:
        #     return "error"
    else: 
        return data
    
# def validateForm(
#     startMonth,
#     endMonth,
#     startYear,
#     endYear,
# ):
    
#     try:
#         startDate = dt.datetime(
#             day=int(startDay),
#             month=int(monthsDict()[startMonth]),
#             year=int(startYear),
#         )
#         endDate = dt.datetime(
#             day=int(endDay), month=int(monthsDict()[endMonth]), year=int(endYear)
#         )
#         maxDate = dt.datetime(day=int(dayList()[0]), month=int(monthsDict()[monthList()[-1]]), year=int(yearList()[0]))     
#     except:
#         messagebox.showinfo("showinfo", "Invalid Date, select again")
    
#     if len(firstRegion) and len(secondRegion):
#         if firstRegion == secondRegion:
#             return messagebox.showinfo("showinfo", "Invalid selection cannot compare same region")
    
#     if startDate > endDate:
#        return messagebox.showinfo("showinfo", "Invalid Date selected(start date cannot be greater than end date!!!!)")

#     elif (startDate > maxDate) or (endDate > maxDate):
#         return messagebox.showinfo("showinfo", "Invalid Date selected")
    
#     else:
#         return startDate, endDate
  
        
def ageRange(month, year, policeForce):
    df = pd.DataFrame.from_dict(isRequestEmpty(month, year, policeForce))
    data = df.groupby(['age_range'], as_index=False).count()
    title = "Stop and Search Cases Breakdown by Age Range for " + policeForce + " in " + month + ", " + year
    pieChart(title, data["involved_person"], data["age_range"])
    
ylabel="Number of Persons Involved"

def searchPurpose(month, year, policeForce):
    df = pd.DataFrame.from_dict(isRequestEmpty(month, year, policeForce))
    data = df.groupby(["object_of_search"], as_index=False)[["involved_person"]].count()
    maxValue=data.max()
    max = maxValue['involved_person'] #gets the max value in the dataFrame
    title = "Stop and Search Cases Breakdown by Search Purpose for " + policeForce + " in " + month + ", " + year
    
    dotPlot(data.index, data["involved_person"], data["object_of_search"], max, ylabel, title=title)
    
    
def ethnicity(month, year, policeForce):
    df = pd.DataFrame.from_dict(isRequestEmpty(month, year, policeForce))
    data = df.groupby(["officer_defined_ethnicity"], as_index=False)[["involved_person"]].count()
    maxValue=data.max()
    max = maxValue['involved_person'] #gets the max value in the dataFrame
    title = "Stop and Search Cases Breakdown by Ethnicity for " + policeForce + " in " + month + ", " + year

    lollipopChart(data.index, data["involved_person"], data["officer_defined_ethnicity"], max, ylabel, title=title, data=data)
    
# def plotViewRangeCases(startMonth, endMonth, startYear, endYear, policeForce):
    
#     validate = validateForm(1, 1, startMonth, endMonth, startYear, endYear)
    
#     if type(validate) is tuple: 
#         startDate = validate[0]
#         endDate = validate[1]
        
#         dateRange = pd.period_range(start=startDate, end=endDate, freq="M").tolist()
#         print(dateRange)

#         data_dict = {}
#         count = 0
#         for date in dateRange:
#             data_dict[count] = [
#                 str(date),
#                 fetchCasesRequest(policeForce, str(date)),
#             ]
#             count += 1

#         df = pd.DataFrame.from_dict(
#             data_dict, orient="index", columns=["Month", "Cases"]
#         )
        
#         # print(df["Cases"])
#         # print(type(df["Cases"]), 'class')
#         # print(df["Month"], 'Month')
        
#         # label = df["Month"]
#         # data = df["Cases"]
#         title = "Stop and Search Cases for " + policeForce + " between " 
#         # + startDate + ", " + endDate
        
#         barChart(df, title, x="Month", y="Cases")
#         # horizontalBarChart( df, label, title)
    
#     # data = df.groupby(["officer_defined_ethnicity"], as_index=False)[["involved_person"]].count()
#     # maxValue=data.max()
#     # max = maxValue['involved_person'] #gets the max value in the dataFrame
#     # title = "Stop and Search Cases for " + policeForce + " between " + startDate + ", " + endDate

#     # lollipopChart(data.index, data["involved_person"], data["officer_defined_ethnicity"], max, ylabel, title=title, data=data)
