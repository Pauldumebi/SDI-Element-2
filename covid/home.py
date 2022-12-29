import tkinter as tkt
from helpers.label import label
from helpers.dropdown import dropdown
from covid.func import plot_total_no_of_cases_each_day, plot_total_no_of_cases_each_month, plot_areas_with_highest_cases, plot_comparing_two_areas
from helpers.regions import region_list
from helpers.destroy import destroy

days = list(range(1, 32))
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
year = [2020]

def total_no_of_cases_each_day(frame_1): 
    destroy(frame_1)

    label(frame_1, "Start Day", x=20, y=50)
    start_day = tkt.StringVar(frame_1)
    
    # select a default value for the dropdown
    start_day.set(days[0]) 
    dropdown(frame_1, start_day, days, x=20, y=70)
    
    label(frame_1, "End Day", x=210, y=50)
    end_day = tkt.StringVar(frame_1)
    end_day.set(days[1])
    dropdown(frame_1, end_day, days, x=210, y=70)
    
    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    
    label(frame_1, "Start Month", x=20, y=120)
    start_month = tkt.StringVar(frame_1)
    start_month.set(months[0])
    dropdown(frame_1, start_month, months, x=20, y=140)
    
    label(frame_1, "End Month", x=210, y=120)
    end_month = tkt.StringVar(frame_1)
    end_month.set(months[1])
    dropdown(frame_1, end_month, months, x=210, y=140)
    
    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    
    label(frame_1, "Start Year", x=20, y=190)
    start_year = tkt.StringVar(frame_1)
    start_year.set(year[0])
    dropdown(frame_1, start_year, year, x=20, y=210)
    
    label(frame_1, "End Year", x=210, y=190)
    end_year = tkt.StringVar(frame_1)
    end_year.set(year[0])
    dropdown(frame_1, end_year, year, x=210, y=210)
    
    func = lambda: plot_total_no_of_cases_each_day(
        start_day.get(),
        end_day.get(),
        start_month.get(),
        end_month.get(),
        start_year.get(),
        end_year.get()
    )
    
    tkt.Button(frame_1, text="view" , command=func).place(x=120, y=280)
    
def total_no_of_cases_each_month(frame_1):
    destroy(frame_1)
        
    start_month_arr = ["January"]
    end_month_arr = ["December"]
    
    label(frame_1, "Start Month", x=100, y=50)
    start_month = tkt.StringVar(frame_1)
    start_month.set(start_month_arr[0]) 
    dropdown(frame_1, start_month, start_month_arr, x=100, y=70)
    
    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''

    
    label(frame_1, "End Month", x=100, y=120)
    end_month = tkt.StringVar(frame_1)
    end_month.set(end_month_arr[0])
    dropdown(frame_1, end_month, end_month_arr, x=100, y=140)
    
    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    
    func = lambda: plot_total_no_of_cases_each_month(
        start_month.get(),
        end_month.get(),
    )
    
    tkt.Button(frame_1, text="view" , command=func).place(x=100, y=200)

def areas_with_highest_cases(frame_1):
    destroy(frame_1)
     
    label(frame_1, "Start Day", x=100, y=50)
    start_day = tkt.StringVar(frame_1)
    start_day.set(days[0]) 
    dropdown(frame_1, start_day, days, x=100, y=70)
    
    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''
        
    label(frame_1, "Start Month", x=100, y=120)
    start_month = tkt.StringVar(frame_1)
    start_month.set(months[0])
    dropdown(frame_1, start_month, months, x=100, y=140)
    
    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    
    label(frame_1, "Start Year", x=100, y=190)
    start_year = tkt.StringVar(frame_1)
    start_year.set(year[0])
    dropdown(frame_1, start_year, year, x=100, y=210)
    
    func = lambda: plot_areas_with_highest_cases(
        start_day.get(),
        start_month.get(),
        start_year.get(),
    )
    
    tkt.Button(frame_1, text="view" , command=func).place(x=100, y=260)
    

def comparing_two_areas(frame_1):
    destroy(frame_1)
    
    label(frame_1, "Start Day", x=20, y=50)
    start_day = tkt.StringVar(frame_1)
    
    # select a default value for the dropdown
    start_day.set(days[0]) 
    dropdown(frame_1, start_day, days, x=20, y=70)
    
    label(frame_1, "End Day", x=210, y=50)
    end_day = tkt.StringVar(frame_1)
    end_day.set(days[1])
    dropdown(frame_1, end_day, days, x=210, y=70)
    
    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    
    label(frame_1, "Start Month", x=20, y=120)
    start_month = tkt.StringVar(frame_1)
    start_month.set(months[0])
    dropdown(frame_1, start_month, months, x=20, y=140)
    
    label(frame_1, "End Month", x=210, y=120)
    end_month = tkt.StringVar(frame_1)
    end_month.set(months[1])
    dropdown(frame_1, end_month, months, x=210, y=140)
    
    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    
    label(frame_1, "Start Year", x=20, y=190)
    start_year = tkt.StringVar(frame_1)
    start_year.set(year[0])
    dropdown(frame_1, start_year, year, x=20, y=210)
    
    label(frame_1, "End Year", x=210, y=190)
    end_year = tkt.StringVar(frame_1)
    end_year.set(year[0])
    dropdown(frame_1, end_year, year, x=210, y=210)
    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    
    label(frame_1, "First Region", x=20, y=260)
    first_region = tkt.StringVar(frame_1)
    first_region.set(region_list()[0])
    dropdown(frame_1, first_region, region_list(), x=20, y=280)
    
    label(frame_1, "Second Region", x=210, y=260)
    second_region = tkt.StringVar(frame_1)
    second_region.set(region_list()[1])
    dropdown(frame_1, second_region, region_list(), x=210, y=280)
    
    
    func = lambda: plot_comparing_two_areas(
        start_day.get(),
        end_day.get(),
        start_month.get(),
        end_month.get(),
        start_year.get(),
        end_year.get(),
        first_region.get(),
        second_region.get()
    )
    
    tkt.Button(frame_1, text="view" , command=func).place(x=120, y=320)