import tkinter as tkt
from helpers.label import label
from helpers.dropdown import dropdown
from stop_and_search.func import plot_stop_and_search_by_months, plot_compare_stop_and_search_results_for_two_areas, plot_ethnicity, plot_by_gender
from helpers.destroy import destroy
from stop_and_search.request import police_force, crime_categories

days = list(range(1, 32))
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
stop_and_search_year_list = ["2020", "2021", "2022"]

def stop_and_search_by_months(frame_1):
    destroy(frame_1)
    
    label(frame_1, "Month", x=50, y=50)
    month = tkt.StringVar(frame_1)
    month.set(months[0]) 
    dropdown(frame_1, month, months, x=50, y=70)
    
    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''

    label(frame_1, "Year", x=50, y=120)
    year = tkt.StringVar(frame_1)
    year.set(stop_and_search_year_list[0])
    dropdown(frame_1, year, stop_and_search_year_list, x=50, y=140)
    
    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    
    all_police_forces = list(police_force().keys())
    label(frame_1, "Police Force", x=50, y=190)
    police_force_list = tkt.StringVar(frame_1)
    police_force_list.set(all_police_forces[0])
    dropdown(frame_1, police_force_list, all_police_forces, x=50, y=210)
    
    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    
    func = lambda: plot_stop_and_search_by_months(
        month.get(),
        year.get(),
        police_force_list.get()
    )
    
    tkt.Button(frame_1, text="view" , command=func).place(x=50, y=260)
    
def compare_stop_and_search_results_for_two_areas(frame_1):
    destroy(frame_1)
    
    label(frame_1, "Year", x=50, y=50)
    year = tkt.StringVar(frame_1)
    year.set(stop_and_search_year_list[0]) 
    dropdown(frame_1, year, stop_and_search_year_list, x=50, y=70)
    
    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''

    label(frame_1, "Year", x=50, y=120)
    year = tkt.StringVar(frame_1)
    year.set(stop_and_search_year_list[0])
    dropdown(frame_1, year, stop_and_search_year_list, x=50, y=140)
    
    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    all_police_forces = list(police_force().keys())
    label(frame_1, "First Police Force", x=50, y=120)
    first_police_force_list = tkt.StringVar(frame_1)
    first_police_force_list.set(all_police_forces[0])
    dropdown(frame_1, first_police_force_list, all_police_forces, x=50, y=140)
    
    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    
    all_police_forces = list(police_force().keys())
    label(frame_1, "Second Police Force", x=50, y=190)
    second_police_force_list = tkt.StringVar(frame_1)
    second_police_force_list.set(all_police_forces[1])
    dropdown(frame_1, second_police_force_list, all_police_forces, x=50, y=210)
    
    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    
    func = lambda: plot_compare_stop_and_search_results_for_two_areas(
        year.get(),
        first_police_force_list.get(),
        second_police_force_list.get()
    )
    
    tkt.Button(frame_1, text="view" , command=func).place(x=50, y=260)
    
def ethnicity(frame_1):
    destroy(frame_1)
    
    label(frame_1, "Month", x=50, y=50)
    months_list = tkt.StringVar(frame_1)
    months_list.set(months[0]) 
    dropdown(frame_1, months_list, months, x=50, y=70)
    
    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''

    label(frame_1, "Year", x=50, y=120)
    year = tkt.StringVar(frame_1)
    year.set(stop_and_search_year_list[0])
    dropdown(frame_1, year, stop_and_search_year_list, x=50, y=140)
    
    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    all_police_forces = list(police_force().keys())
    label(frame_1, "Police Force", x=50, y=190)
    police_force_list = tkt.StringVar(frame_1)
    police_force_list.set(all_police_forces[0])
    dropdown(frame_1, police_force_list, all_police_forces, x=50, y=210)
    
    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    
    func = lambda: plot_ethnicity(
        months_list.get(),
        year.get(),
        police_force_list.get(),
    )
    
    tkt.Button(frame_1, text="view" , command=func).place(x=50, y=260)
    
def by_gender(frame_1):
    destroy(frame_1)
    
    label(frame_1, "Months", x=50, y=50)
    month_list = tkt.StringVar(frame_1)
    month_list.set(months[0]) 
    dropdown(frame_1, month_list, months, x=50, y=70)
    
    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''

    label(frame_1, "Year", x=50, y=120)
    year = tkt.StringVar(frame_1)
    year.set(stop_and_search_year_list[0])
    dropdown(frame_1, year, stop_and_search_year_list, x=50, y=140)
    
    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    
    all_police_forces = list(police_force().keys())
    label(frame_1, "First Police Force", x=50, y=190)
    police_force_list = tkt.StringVar(frame_1)
    police_force_list.set(all_police_forces[0])
    dropdown(frame_1, police_force_list, all_police_forces, x=50, y=210)
    
    
    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    
    # all_crime_categories = list(crime_categories().values())
    # label(frame_1, "Second Police Force", x=50, y=190)
    # crime_categories_list = tkt.StringVar(frame_1)
    # crime_categories_list.set(all_crime_categories[0])
    # dropdown(frame_1, crime_categories_list, all_crime_categories, x=50, y=210)
    
    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    
    func = lambda: plot_by_gender(
        month_list.get(),
        year.get(),
        police_force_list.get()
    )
    
    tkt.Button(frame_1, text="view" , command=func).place(x=50, y=260)
