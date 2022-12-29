from tkinter import *
import pandas as pd
from tkinter import messagebox
import numpy as np
import datetime as dt
from utils.filterParams import regionList
from utils.monthsDict import monthsDict
from charts.index import groupBarChart, horizontalBarChart, areaChart, TreeMap
from utils.validateForm import validateForm

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
    
def isDataEmpty(data):
    if(len(data) <= 0):
        return messagebox.showinfo("showinfo", "No data available for this period, select again")
    else:
        return len(data)
        
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
        title =  "Top regions with the highest cases from " + startDay + "/" + monthsDict()[startMonth] + "/" + startYear + " to " + endDay + "/" + monthsDict()[endMonth] + "/" + endYear

        mask = (df['date'] >= startDate) & (df['date'] <= endDate)
        if isDataEmpty(mask) > 1:
            areaNameSum = df.loc[mask]
            areaNameSum = areaNameSum.groupby(['areaName'], as_index=False)[['newCasesBySpecimenDate-Total']].sum()
            areaNameSum =   areaNameSum.loc[(areaNameSum["areaName"] != "United Kingdom") & (areaNameSum["areaName"] != "England")].sort_values(['newCasesBySpecimenDate-Total'], ascending=False)
            areaNameSum =   areaNameSum.loc[areaNameSum["newCasesBySpecimenDate-Total"] > 0] 
            data = areaNameSum[["areaName","newCasesBySpecimenDate-Total"]][:20]
            size = data["newCasesBySpecimenDate-Total"].values.tolist()# proportions of the categories
            labels = data.apply(lambda x: str(x[0]) + "\n (" + str(x[1]) + ")", axis=1)
            TreeMap( title, size, labels )

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
       
   
        
        if case == "Daily infection rate":
            title =  "Daily Cases for " + region + " from " + startDay + "/" +  monthsDict()[startMonth] + "/" + startYear + " to " + endDay + "/" + monthsDict()[endMonth] + "/" + endYear
            areaChart(
                # newWindow, 
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
            areaChart(
                # newWindow, 
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
    title =  "Cases by age group between " + firstRegion + " and " + secondRegion + " from " + startDay + "/" + monthsDict()[startMonth] + "/" + startYear + " to " + endDay + "/" + monthsDict()[endMonth] + "/" + endYear
    
    if type(validate) is tuple: 
        startDate = validate[0]
        endDate = validate[1]
        data = df.loc[(df['date'] >= startDate) & (df['date'] <= endDate)] #slice and get values between start and end date.
        data = data[data['areaName'].isin([firstRegion, secondRegion])]
        data = data.groupby(['areaName'], as_index=False)[['newCasesBySpecimenDate-0_59', 'newCasesBySpecimenDate-60+']].sum()
        data =   data.sort_values(['newCasesBySpecimenDate-0_59', 'newCasesBySpecimenDate-60+'], ascending=False)
        data = data[["areaName","newCasesBySpecimenDate-0_59","newCasesBySpecimenDate-60+"]]
        if isDataEmpty(data) > 1:
            groupBarChart(title, data, "areaName", "Cases", ["Age Group 0-59", "Age Group 60+"])
    
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
    title =  "Regions with the highest cases in the month of " + month + ", " + year
    horizontalBarChart( data, groupLabel, title)
        
    return
