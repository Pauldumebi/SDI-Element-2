from stop_and_search.request import police_force, get_cases
from helpers.form_validator import month_calendar;
from tkinter import messagebox
import pandas as pd
from charts import area_chart, group_bar_chart, colored_bar_chart, pie_chart, donut_chart, scatter_plot
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import seaborn as sns

def is_request_empty(month, year, selected_police_force):
    date = year + "-" + month_calendar()[month]
    # This list contains two items, the data and the length
    result = get_cases(selected_police_force, date)[1]
    if result == []:
        messagebox.showinfo("showinfo", "No data for this selected month")
    else: 
        return result
    
def plot_stop_and_search_by_months(month, year, selected_police_force):    
    stop_and_search_df = pd.DataFrame.from_dict(is_request_empty(month, year, selected_police_force))
    result = stop_and_search_df.groupby(['age_range'], as_index=False).count()
    title = "Stop and search by Age Range for " + selected_police_force + " in " + month + ", " + year
    donut_chart(title, result["involved_person"], result["age_range"])
    # print(result, 'result')

def plot_compare_stop_and_search_results_for_two_areas(year, first_police_force, second_police_force):
    summer_months = ["June", "July", "August"]

    first_data_dict = {}

    count = 0
    for month in summer_months:
        first_data_dict[count] = [
            month,
            is_request_empty(month, year, first_police_force),
        ]
        count += 1 
    
    # stop_and_search_df = pd.DataFrame.from_dict(is_request_empty(month, year, selected_police_force))
    # stop_and_search_df_first = pd.DataFrame.from_dict(first_data_dict)
    stop_and_search_df_first = pd.DataFrame.from_dict(
            first_data_dict, orient="index", columns=["Month", "Cases Count"]
        )
    # Arrest
            
    print(stop_and_search_df_first, 'stop_and_search_df_first')
    
    
    count_cases = stop_and_search_df_first[stop_and_search_df_first['Cases Count'].apply(lambda x: x[0]['age_range']=='18-24')]
    print(count_cases, 'count_cases')
    
    # first_result = stop_and_search_df_first.groupby(['age_range'], as_index=False).count()
    # print(first_result, 'first_result')
    
    # second_data_dict = {}
    # count = 0
    # for month in summer_months:
    #     second_data_dict[count] = [
    #         month,
    #         is_request_empty(month, year, second_police_force),
    #     ]
    #     count += 1 
    # stop_and_search_df_2 = pd.DataFrame.from_dict(second_data_dict)
    # second_result = stop_and_search_df_2.groupby(['age_range'], as_index=False).count()
    # print(second_result)


def plot_ethnicity(month, year, selected_police_force):   
 
    stop_and_search_df = pd.DataFrame.from_dict(is_request_empty(month, year, selected_police_force))
    result = stop_and_search_df.groupby(["officer_defined_ethnicity"], as_index=False)[["involved_person"]].count()
    # maxValue=data.max()
    # max = maxValue['involved_person'] #gets the max value in the dataFrame
    title = "Stop and Search Cases Breakdown by Ethnicity for " + selected_police_force + " in " + month + ", " + year
    scatter_plot(title, result["officer_defined_ethnicity"], result["involved_person"])
    
    # print(result, 'result')

    # lollipopChart(data.index, data["involved_person"], data["officer_defined_ethnicity"], max, ylabel, title=title, data=data)

def plot_by_gender(month, year, selected_police_force):    

    stop_and_search_df = pd.DataFrame.from_dict(is_request_empty(month, year, selected_police_force))
    result = stop_and_search_df.groupby(['gender'], as_index=False).count()
    title = "Stop and search breakdown of by gender for " + selected_police_force + " in " + month + ", " + year
    pie_chart(title, result["involved_person"], result["gender"])
