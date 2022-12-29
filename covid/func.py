import pandas as pd
import numpy as np
from helpers.form_validator import form_validator
from tkinter import messagebox
from charts import area_chart, group_bar_chart, colored_bar_chart, pie_chart

covid_data_frame = pd.read_csv('specimenDate_ageDemographic-unstacked.csv', low_memory=False)

#The only columns needed for this visualizations are the ones listed below
covid_data_frame = covid_data_frame[["areaType", "areaCode", "areaName", "date", "newCasesBySpecimenDate-0_59", "newCasesBySpecimenDate-60+"]]

# Total number of cases each day
covid_data_frame["newCasesBySpecimenDate-Total"] = (covid_data_frame["newCasesBySpecimenDate-0_59"] + covid_data_frame["newCasesBySpecimenDate-60+"])

# This is to convert date column to datetime object
covid_data_frame["date"] = pd.to_datetime(covid_data_frame["date"])

# This is to replace all missing values with 0
covid_data_frame.replace([np.inf, -np.inf], np.nan, inplace=True)
covid_data_frame.fillna(0, inplace=True)

# This is to get the percent change in infection rate per day
covid_data_frame["%changeInfectionRate-Total"] = (covid_data_frame.groupby("areaName")["newCasesBySpecimenDate-Total"].pct_change() * 100)
covid_data_frame["%changeInfectionRate-0_59"] = (covid_data_frame.groupby("areaName")["newCasesBySpecimenDate-0_59"].pct_change() * 100)
covid_data_frame["%changeInfectionRate-60+"] = (covid_data_frame.groupby("areaName")["newCasesBySpecimenDate-60+"].pct_change() * 100)

def is_array_empty(covid_data):
    if(len(covid_data) <= 0):
            return messagebox.showinfo("showinfo", "No data available for this range, select again")


def plot_total_no_of_cases_each_day(start_day, end_day, start_month, end_month, start_year, end_year):
    
    date = form_validator(start_day, end_day, start_month, end_month, start_year, end_year)
        
    if type(date) is tuple: 
        start_date = date[0]
        end_date = date[1]
        
        covid_data = covid_data_frame.loc[
            (
                (covid_data_frame["date"] >= start_date)
                & (covid_data_frame["date"] <= end_date)
            )
        ]
        covid_data = covid_data.groupby(["date"], as_index=False)[["newCasesBySpecimenDate-Total", "%changeInfectionRate-Total"]].sum()
        
        is_array_empty(covid_data)
       
        title =  "Daily Cases for from " + start_day + "/" + start_month + "/" + start_year + " to " + end_day + "/" + end_month + "/" + end_year
        area_chart(
            title, 
            "Total Daily Cases", 
            "%Change in Daily Case", 
            covid_data, 
            "date", 
            "newCasesBySpecimenDate-Total", 
            "Total Change in Daily cases", 
            "%changeInfectionRate-Total",
            "Cases", 
            legends=["%Change in Total Daily Case"]
        )         

        return

    
def plot_comparing_two_areas(start_day, end_day, start_month, end_month, start_year, end_year, region_one, region_two):
    date = form_validator(start_day, end_day, start_month, end_month, start_year, end_year)
    if region_one == region_two:
        return messagebox.showinfo("showinfo", "Regions cannot be the same")
    
    if type(date) is tuple: 
        start_date = date[0]
        end_date = date[1]
        title =  "Total Cases between " + region_one + " and " + region_two + " from" +" 01/" + start_month + "/2020" + " to " + " 31/" + end_month + "/" + "2020"
        covid_data = covid_data_frame.loc[
            (
                (covid_data_frame["date"] >= start_date)
                & (covid_data_frame["date"] <= end_date)
            )
        ]
        covid_data = covid_data.groupby(["areaName"], as_index=False)[["newCasesBySpecimenDate-Total", "%changeInfectionRate-Total"]].sum()
        covid_data = covid_data.loc[(covid_data['areaName'] == region_one) | (covid_data['areaName'] == region_two)].sort_values(["newCasesBySpecimenDate-Total"],ascending=False)
        print(covid_data)
        
        is_array_empty(covid_data)
        if len(covid_data) > 1:
            pie_chart(title, covid_data["newCasesBySpecimenDate-Total"], covid_data["areaName"])
    
def plot_total_no_of_cases_each_month( start_month, end_month ):
    
    date = form_validator(
        start_day="1", 
        end_day="31", 
        start_month=start_month, 
        end_month=end_month, 
        start_year="2020", 
        end_year="2020"
    )
    
    title =  "Cases by age group from " + "01/" + start_month + "/2020" + " to " + "31/" + end_month + "/" + "2020"
    
    if type(date) is tuple: 
        start_date = date[0]
        end_date = date[1]
        #Get values between start and end date.
        covid_data = covid_data_frame.loc[(covid_data_frame['date'] >= start_date) & (covid_data_frame['date'] <= end_date)]
        covid_data = covid_data.groupby(covid_data['date'].dt.strftime('%m-%y')).agg(total_cases = ('newCasesBySpecimenDate-Total' , 'sum'))
        # covid_data.set_index('date')
        # covid_data = covid_data.groupby([lambda x: x.year, lambda x: x.month]).sum()
        # data = data.groupby(["date"], as_index=False)[["newCasesBySpecimenDate-Total", "%changeInfectionRate-Total"]].sum()
        # covid_data = covid_data.groupby(covid_data.date.dt.month)['newCasesBySpecimenDate-0_59', 'newCasesBySpecimenDate-60+'].sum()
        # covid_data['date'] = pd.to_datetime(
        # arg=covid_data['date'],
        # format='%d-%b-%y' # Assuming dd-Mon-yy format
        # )

        # # Group by year and month
        # covid_data.groupby(
        # [
        #     covid_data['date'].dt.year,
        #     covid_data['date'].dt.month 
        # ]
        # ).sum()
        # covid_data = covid_data.groupby(pd.TimeGrouper('M'))[['newCasesBySpecimenDate-0_59', 'newCasesBySpecimenDate-60+']].sum()
        # data = data.sort_values(['newCasesBySpecimenDate-0_59', 'newCasesBySpecimenDate-60+'], ascending=False)
        # covid_data = covid_data[["date","newCasesBySpecimenDate-0_59","newCasesBySpecimenDate-60+"]]
        print(covid_data['date'])
        # group_bar_chart( title, covid_data, "date", "Cases", ["Age Group 0-59", "Age Group 60+"])
    
def plot_areas_with_highest_cases(start_day, start_month, start_year):
    date = form_validator(start_day, end_day="1", start_month=start_month, start_year=start_year, end_month="December", end_year="2020")
        
    if type(date) is tuple: 
        start_date = date[0]
        
        covid_data = covid_data_frame.loc[
            (
                (covid_data_frame["date"] == start_date)
            )
        ]
        
        if(len(covid_data) <= 0):
            return messagebox.showinfo("showinfo", "No data available for this day")
        
        covid_data = covid_data.loc[(covid_data["areaName"] != "United Kingdom") & (covid_data["areaName"] != "England")].sort_values(["newCasesBySpecimenDate-Total"],ascending=False)
        covid_data = covid_data[["areaName","newCasesBySpecimenDate-Total"]][:9]
        
        
        title =  "Total cases for " + start_day + "/" + start_month + "/" + start_year 
        colored_bar_chart(covid_data, title, first_label="areaName", second_label="newCasesBySpecimenDate-Total")