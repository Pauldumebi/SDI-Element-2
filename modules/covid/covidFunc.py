from tkinter import *
import pandas as pd
from tkinter import messagebox
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from utils.filterParams import regionList, monthList, yearList, dayList
from utils.monthsDict import monthsDict
from charts.index import groupBarChart, simplePlot, horizontalBarChart, lineChart, TreeMap

df =pd.read_csv('data/specimenDate_ageDemographic-unstacked.csv', low_memory=False)
df = df[["areaType", "areaCode", "areaName", "date", "newCasesBySpecimenDate-0_59", "newCasesBySpecimenDate-60+"]] #select only needed columns

# Total cases per day
df["newCasesBySpecimenDate-Total"] = (df["newCasesBySpecimenDate-0_59"] + df["newCasesBySpecimenDate-60+"])

# Convert date column to datetime object
df["date"] = pd.to_datetime(df["date"])

# get %change% in infection rate per day
df["%changeInfectionRate-Total"] = (df.groupby("areaName")["newCasesBySpecimenDate-Total"].pct_change() * 100)
df["%changeInfectionRate-0_59"] = (df.groupby("areaName")["newCasesBySpecimenDate-0_59"].pct_change() * 100)
df["%changeInfectionRate-60+"] = (df.groupby("areaName")["newCasesBySpecimenDate-60+"].pct_change() * 100)

# Replace missing values with 0
df.replace([np.inf, -np.inf], np.nan, inplace=True)
df.fillna(0, inplace=True)

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
       return messagebox.showinfo("showinfo", "Invalid Date selected(start date cannot be greater than end date!!!!)")

    elif (startDate > maxDate) or (endDate > maxDate):
        return messagebox.showinfo("showinfo", "Invalid Date selected")
    
    else:
        return startDate, endDate
    
    
    
def viewTopFiveRegionWithHighestCases(
    startDay,
    endDay,
    startMonth,
    endMonth,
    startYear,
    endYear,
):
    validate = validateForm(startDay, endDay, startMonth, endMonth, startYear, endYear)
    
    if type(validate) is tuple: 
        startDate = validate[0]
        endDate = validate[1]
    
        # newWindow = Toplevel()
        # newWindow.geometry("+%d+%d" % (250, 10))
        # title =  "Top 5 regions with the highest cases from " + startDay + "/" + monthsDict()[startMonth] + "/" + startYear + " to " + endDay + "/" + monthsDict()[endMonth] + "/" + endYear
        # newWindow.title(title)

        mask = (df['date'] >= startDate) & (df['date'] <= endDate)
        areaNameSum = df.loc[mask]
        # areaNameSum = areaNameSum.groupby(['areaName'], as_index=False)[['newCasesBySpecimenDate-0_59', 'newCasesBySpecimenDate-60+']].sum()
        # areaNameSum =   areaNameSum.loc[(areaNameSum["areaName"] != "United Kingdom") & (areaNameSum["areaName"] != "England")].sort_values(['newCasesBySpecimenDate-0_59', 'newCasesBySpecimenDate-60+'], ascending=False)
        # data = areaNameSum[["areaName","newCasesBySpecimenDate-0_59","newCasesBySpecimenDate-60+"]][:5]
        areaNameSum = areaNameSum.groupby(['areaName'], as_index=False)[['newCasesBySpecimenDate-Total']].sum()
        areaNameSum =   areaNameSum.loc[(areaNameSum["areaName"] != "United Kingdom") & (areaNameSum["areaName"] != "England")].sort_values(['newCasesBySpecimenDate-Total'], ascending=False)
        areaNameSum =   areaNameSum.loc[areaNameSum["newCasesBySpecimenDate-Total"] > 0] 
        data = areaNameSum[["areaName","newCasesBySpecimenDate-Total"]][:20]
        size = data["newCasesBySpecimenDate-Total"].values.tolist()# proportions of the categories
        labels = data.apply(lambda x: str(x[0]) + "\n (" + str(x[1]) + ")", axis=1)
        TreeMap( df, path="areaName", values="newCasesBySpecimenDate-Total", 
                # size, labels
                )
        # groupBarChart(newWindow, title, data, "areaName", "Cases Count", ["Age Group 0-59", "Age Group 60+"])

        return

def plotDailyCases(
    case,
    startDay,
    endDay,
    startMonth,
    endMonth,
    startYear,
    endYear,
    region,
    # test=False
):
    validate = validateForm(startDay, endDay, startMonth, endMonth, startYear, endYear)
    
    if region not in regionList():
        return messagebox.showinfo("showinfo", "The region selected isn't available")
        
    if type(validate) is tuple: 
        startDate = validate[0]
        endDate = validate[1]
        
        data = df.loc[
            (
                (df["areaName"] == region)
                & (df["date"] >= startDate)
                & (df["date"] <= endDate)
            )
        ]
        
        if(len(data) <= 0):
            return messagebox.showinfo("showinfo", "No data available for this range")
       
        newWindow = Toplevel()
        
        if case == "Daily infection rate":
            title =  "Daily Cases for " + region + " from " + startDay + "/" +  monthsDict()[startMonth] + "/" + startYear + " to " + endDay + "/" + monthsDict()[endMonth] + "/" + endYear
            lineChart(
                newWindow, 
                title, 
                "Total Daily Cases", 
                "Daily Case By Age Group", 
                data, 
                "date", 
                "newCasesBySpecimenDate-Total", 
                "Total Daily Cases", 
                "newCasesBySpecimenDate-0_59", 
                "newCasesBySpecimenDate-60+", 
                "Cases", 
                legends=["Age Group 0-59", "Age Group 60+"]
            )        
        else: 
            title = "%Change in Total Daily Cases for " + region + " from " + startDay + "/" +  monthsDict()[startMonth] + "/" + startYear + " to " + endDay + "/" + monthsDict()[endMonth] + "/" + endYear
            lineChart(
                newWindow, 
                title, 
                "%Change in Total Daily Cases", 
                "%Change of Daily Case By Age Group", 
                data, 
                "date", 
                "%changeInfectionRate-Total", 
                "Total Daily Cases", 
                "%changeInfectionRate-0_59", 
                "%changeInfectionRate-60+", 
                "Cases", 
                legends=["Age Group 0-59", "Age Group 60+"]
            )
            
        
        newWindow.geometry("+%d+%d" % (250, 10))
        newWindow.title(title)
        return


def plotTwoRegions(
    startDay,
    endDay,
    startMonth,
    endMonth,
    startYear,
    endYear,
    firstRegion,
    secondRegion
): 
    validate = validateForm(startDay, endDay, startMonth, endMonth, startYear, endYear, firstRegion, secondRegion)
    title =  "Total cases between " + firstRegion + " and " + secondRegion + " from " + startDay + "/" + monthsDict()[startMonth] + "/" + startYear + " to " + endDay + "/" + monthsDict()[endMonth] + "/" + endYear
    # newWindow = Toplevel()
    # newWindow.geometry("+%d+%d" % (250, 10))
    # newWindow.title(title)
    
    # TreeMap(newWindow)
    if type(validate) is tuple: 
        startDate = validate[0]
        endDate = validate[1]
        
        data = df.loc[(df['date'] >= startDate) & (df['date'] <= endDate)] #slice and get values between start and end date.
        data = data[data['areaName'].isin([firstRegion, secondRegion])]
        # data = data.loc[(data["areaName"] == firstRegion) & (data["areaName"] == secondRegion)]
        # firstRegionData = data.loc[data['areaName'] == firstRegion, 'newCasesBySpecimenDate-Total']
        # secondRegionData = data.loc[data['areaName'] == secondRegion, 'newCasesBySpecimenDate-Total']
        # areaName = data.loc[data['areaName'] == firstRegion]
        
        # print(len(firstRegionData), 'firstRegionData')
        # print(len(secondRegionData), 'secondRegionData')
        
        # print(data["newCasesBySpecimenDate-Total"], 'newCasesBySpecimenDate-Total')
        # newCasesBySpecimenDate-Total
        # df2 = df.groupby('class').size().reset_index(name='areaName')
        df_raw = pd.read_csv("https://github.com/selva86/datasets/raw/master/mpg_ggplot2.csv")

        # Prepare Data
        df_raw = df_raw.groupby('class').size().reset_index(name='counts')
        print(df_raw)
        newWindow = Toplevel()
        newWindow.geometry("+%d+%d" % (250, 10))
        newWindow.title(title)
        # N, x, y
        # TreeMap(newWindow, df_raw)
        # simplePlot(newWindow, title, firstRegionData, secondRegionData)
        
    #     return
    
def plotByMonths(
    month,
    year,
): 

    monthNo = 0
    
    if 1 <= int(monthsDict()[month]) <= 9:
       monthNo =  "0" + monthsDict()[month]
    else:
        monthNo = monthsDict()[month]
        
    monthYearOnly = year + '-' + monthNo
    data = pd.read_csv('data/specimenDate_ageDemographic-unstacked.csv', low_memory=False)
    data["newCasesBySpecimenDate-Total"] = (data["newCasesBySpecimenDate-0_59"] + data["newCasesBySpecimenDate-60+"])
    data = data.loc[data.date.str[0:7] == monthYearOnly]
    data = data.groupby(['areaName'], as_index=False)[["newCasesBySpecimenDate-Total"]].sum()
    data = data.loc[(data["areaName"] != "United Kingdom") & (data["areaName"] != "England")].sort_values(["newCasesBySpecimenDate-Total"],ascending=False)

    groupLabel = data["areaName"][:20]
    data = data["newCasesBySpecimenDate-Total"][:20]
    
    newWindow = Toplevel()
    newWindow.geometry("+%d+%d" % (250, 10))
    title =  "Regions with the highest cases in the month of " + month + year
    newWindow.title(title)
    
    horizontalBarChart(newWindow, data, groupLabel)
        
    return